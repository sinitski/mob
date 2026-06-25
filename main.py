import flet as ft
import httpx
import time
import json
from datetime import datetime
import threading


def main(page: ft.Page):
    page.title = "Webhook Sender"
    page.window_width = 400
    page.window_height = 600
    
    # Webhook URL
    WEBHOOK_URL = "https://eug3.vercel.app/webhook/8531859495:AAHZusQJdMslQ3nQ7yCI1jcBkUwKp9g_nsk"
    
    # Status messages
    status_text = ft.Text(value="Ready", size=14, color=ft.colors.GREY)
    
    # Input field
    input_field = ft.TextField(
        label="Enter number (+ optional comment)",
        multiline=False,
        min_lines=1,
        max_lines=1,
        border_color=ft.colors.BLUE_400,
        focused_border_color=ft.colors.BLUE_700,
        width=350,
    )
    
    # Comment field
    comment_field = ft.TextField(
        label="Comment (optional)",
        multiline=True,
        min_lines=2,
        max_lines=5,
        border_color=ft.colors.BLUE_400,
        focused_border_color=ft.colors.BLUE_700,
        width=350,
    )
    
    # Progress indicator
    progress_ring = ft.ProgressRing(visible=False, width=30, height=30)
    
    def send_webhook(e=None):
        """Send data to webhook"""
        text_value = input_field.value.strip()
        comment_value = comment_field.value.strip()
        
        if not text_value:
            status_text.value = "❌ Please enter a number"
            status_text.color = ft.colors.RED
            page.update()
            return
        
        # Combine text and comment
        if comment_value:
            full_text = f"{text_value} {comment_value}"
        else:
            full_text = text_value
        
        # Update UI
        progress_ring.visible = True
        status_text.value = "📤 Sending..."
        status_text.color = ft.colors.ORANGE
        page.update()
        
        def send_async():
            try:
                # Prepare JSON payload
                current_time = int(time.time())
                payload = {
                    "update_id": current_time,
                    "message": {
                        "message_id": 1,
                        "from": {
                            "id": 789161700,
                            "is_bot": False,
                            "first_name": "Eugene",
                            "username": "eugn3"
                        },
                        "chat": {
                            "id": 789161700,
                            "type": "private"
                        },
                        "date": current_time,
                        "text": full_text
                    }
                }
                
                # Send POST request
                response = httpx.post(
                    WEBHOOK_URL,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=10.0
                )
                
                # Update UI with result
                if response.status_code in [200, 201]:
                    status_text.value = f"✅ Sent! (ID: {current_time})"
                    status_text.color = ft.colors.GREEN
                    input_field.value = ""
                    comment_field.value = ""
                else:
                    status_text.value = f"⚠️ Response: {response.status_code}"
                    status_text.color = ft.colors.ORANGE
                
            except Exception as ex:
                status_text.value = f"❌ Error: {str(ex)}"
                status_text.color = ft.colors.RED
            
            finally:
                progress_ring.visible = False
                page.update()
        
        # Run in background thread to prevent blocking UI
        threading.Thread(target=send_async, daemon=True).start()
    
    # Send button
    send_button = ft.ElevatedButton(
        text="Send",
        on_click=send_webhook,
        width=350,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )
    
    # History display
    history_text = ft.Text(value="No messages sent yet", size=12, color=ft.colors.GREY)
    
    def clear_history(e):
        history_text.value = "History cleared"
        page.update()
    
    clear_button = ft.IconButton(
        icon=ft.icons.DELETE,
        on_click=clear_history,
    )
    
    # Layout
    column = ft.Column(
        controls=[
            ft.Container(
                content=ft.Text("Webhook Sender", size=24, weight="bold"),
                padding=20,
            ),
            ft.Divider(),
            ft.Container(
                content=input_field,
                padding=10,
            ),
            ft.Container(
                content=comment_field,
                padding=10,
            ),
            ft.Container(
                content=ft.Row(
                    controls=[
                        send_button,
                        progress_ring,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=10,
            ),
            ft.Container(
                content=status_text,
                padding=10,
                alignment=ft.alignment.center,
            ),
            ft.Divider(),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text("Recent:", size=12, weight="bold"),
                        clear_button,
                    ],
                ),
                padding=10,
            ),
            ft.Container(
                content=history_text,
                padding=10,
            ),
        ],
        scroll=ft.ScrollMode.AUTO,
    )
    
    page.add(column)
    
    # Keyboard support (Enter to send)
    def on_key(e: ft.KeyboardEvent):
        if e.key == "Enter" and not comment_field.focus:
            send_webhook()
    
    page.on_keyboard_event = on_key


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
