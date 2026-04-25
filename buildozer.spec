[app]

# 🔹 معلومات التطبيق
title = EcoTrack AI
package.name = ecotrack
package.domain = org.eco

# 🔹 مصدر الملفات
source.dir = .
source.include_exts = py,png,jpg,kv

# 🔹 الإصدار
version = 1.0

# 🔹 المكتبات
requirements = python3,kivy,kivymd,requests

# 🔹 العرض
orientation = portrait
fullscreen = 0

# 🔹 الصلاحيات
android.permissions = INTERNET

# 🔥 دعم Android الحديث (مهم جدًا)
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.target_sdk_version = 33

# 🔥 تحسين الأداء والتوافق
android.arch = armeabi-v7a, arm64-v8a
android.allow_backup = True

# ❌ نحذف هذه لأنها تسبب مشاكل في GitHub
# android.sdk_path = ...
# android.ndk_path = ...

[buildozer]

log_level = 2
warn_on_root = 1
