from django.db import models

# 마이그레이션 작업 시 자동으로 앱의 이름이 붙게 됨
class Hospital(models.Model): # secondapp_hospital
  # id = models.CharField(max_length=255) 생략가능, 자동 생성
  sido = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  medical = models.CharField(max_length=255)
  room = models.CharField(max_length=255)
  tel = models.CharField(max_length=255)
  address = models.CharField(max_length=255)