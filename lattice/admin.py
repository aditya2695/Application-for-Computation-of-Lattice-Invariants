from django.contrib import admin
from .models import FilesUpload, Lattice,LatticeTypes,lattice_2D_data,lattice_3D_data,FileModel


class LatticeAdmin(admin.ModelAdmin):
    list_display = ("name","length_a","angle_a")

class BravaisAdmin(admin.ModelAdmin):
    list_display = ("name","length_a","angle_a","length_b","angle_b")

class lattice2DAdmin(admin.ModelAdmin):
    list_display = ("id","a","b","gamma")

class lattice3DAdmin(admin.ModelAdmin):
    list_display = ("id","a","b","c","alpha","beta","gamma","bravais_types")

# Register your models here.
admin.site.register(Lattice,LatticeAdmin)
admin.site.register(LatticeTypes,BravaisAdmin)
admin.site.register(lattice_2D_data,lattice2DAdmin)
admin.site.register(lattice_3D_data,lattice3DAdmin)
admin.site.register(FileModel)
admin.site.register(FilesUpload)


