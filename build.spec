# Buildozer spec file for Webhook Sender app
[app]
title = Webhook Sender
package.name = webhooksender
package.domain = org.webhooksender

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy,httpx

# Supported orientations
orientation = portrait

# fullscreen
fullscreen = 0

android.permissions = INTERNET,BIND_APPWIDGET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Enable logcat for debugging
android.logcat_filters = *:S python:D

# Use modern gradle
android.gradle_dependencies = 

# App icon (optional)
icon.filename = %(source.dir)s/data/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
