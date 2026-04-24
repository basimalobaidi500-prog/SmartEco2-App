[app]

title = EcoTrack AI
package.name = ecotrack
package.domain = org.eco

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,kivymd,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# 👇 أضف هذا في آخر الملف
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk

[buildozer]

log_level = 2
warn_on_root = 1
