from django.db import models
from acounts.models import UserProfileInfo


class dataguru(models.Model):
    #id=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, primary_key=True)
    # norole=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE,null=True)
    #noid=models.IntegerField(blank=True,null=False)
    nama=models.CharField(max_length=30)
    nohp=models.CharField(max_length=15)
    alamat=models.CharField(max_length=225,null=True)
    biaya=models.IntegerField(null=True)
    no_id=models.IntegerField(blank=True, null=True)
    #kelamin=models.BooleanField(default=True)
    usia=models.IntegerField(blank=True,null=True)
    link=models.CharField(max_length=500,blank=True,null=True)
    # catatan=models.TextField(null=True)
    img = models.ImageField(upload_to='img',blank=True)
    # portofolio=models.FileField(upload_to='document/')
    

    def __str__(self):
        return self.nama

class datamurid(models.Model):
    #id=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, primary_key=True)
    # norole=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE,null=True)
    #noid=models.IntegerField(blank=True,null=False)
    # dt_id=models.IntegerField(blank=True, null=True)
    nama=models.CharField(max_length=300)
    nohp=models.CharField(max_length=15)
    alamat=models.CharField(max_length=225,null=True)
    
    usia=models.IntegerField(null=True)
    pnd=models.CharField(max_length=300,blank=True)
    no_id=models.IntegerField(blank=True, null=True)
    pendidikan=models.CharField(max_length=200,blank=True)
    # nama=models.CharField(max_length=30)
    # alamat=models.CharField(max_length=225)
    # no=models.CharField(max_length=15)
    # pendidikan=models.ForeignKey(KtgAmpu, on_delete=models.CASCADE, null=True)
    # kelamin=models.BooleanField(default=True)

    def __str__(self):
        return self.nama


# class gurudata(models.Model):
#     nama=models.CharField(max_length=30)
#     nohp=models.CharField(max_length=15)
#     alamat=models.CharField(max_length=225,null=True)
#     pendidikan=models.CharField(max_length=200)
#     no_id=models.IntegerField()

#     def __str__(self):
#         return self.nama

# class siswadata(models.Model):
#     nama=models.CharField(max_length=30)
#     nohp=models.CharField(max_length=15)
#     alamat=models.CharField(max_length=225,null=True)
#     pendidikan=models.CharField(max_length=200)
#     no_id=models.IntegerField()

#     def __str__(self):
#         return self.nama