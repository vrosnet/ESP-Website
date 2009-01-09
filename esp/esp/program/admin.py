__author__    = "MIT ESP"
__date__      = "$DATE$"
__rev__       = "$REV$"
__license__   = "GPL v.2"
__copyright__ = """
This file is part of the ESP Web Site
Copyright (c) 2008 MIT ESP

The ESP Web Site is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

Contact Us:
ESP Web Group
MIT Educational Studies Program,
84 Massachusetts Ave W20-467, Cambridge, MA 02139
Phone: 617-253-4882
Email: web@esp.mit.edu
"""

from django.contrib import admin

from esp.program.models import ProgramModule, ArchiveClass, Program, BusSchedule
from esp.program.models import TeacherParticipationProfile, SATPrepRegInfo, RegistrationProfile
from esp.program.models import TeacherBio, FinancialAidRequest

from esp.program.models import ProgramCheckItem, ClassSection, ClassSubject, ClassCategories

class ProgramModuleAdmin(admin.ModelAdmin):
    list_display = ('link_title', 'admin_title', 'handler', 'main_call')
    search_fields = ['link_title', 'admin_title', 'handler', 'main_call']
admin.site.register(ProgramModule, ProgramModuleAdmin)
    
class ArchiveClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'date', 'category', 'program', 'teacher')
    search_fields = ['description', 'title', 'program', 'teacher', 'category']
    pass
admin.site.register(ArchiveClass, ArchiveClassAdmin)
    
admin.site.register(Program)
admin.site.register(BusSchedule)
admin.site.register(TeacherParticipationProfile)
    
class SATPrepRegInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'program')
    #list_filter = ('program',)
    search_fields = ['user__username']
    pass
admin.site.register(SATPrepRegInfo, SATPrepRegInfoAdmin)

class RegistrationProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'contact_user', 'program')
    pass
admin.site.register(RegistrationProfile, RegistrationProfileAdmin)
    
class TeacherBioAdmin(admin.ModelAdmin):
    list_display = ('user', 'program', 'slugbio')
    search_fields = ['user__username', 'slugbio', 'bio']

admin.site.register(TeacherBio, TeacherBioAdmin)
    
admin.site.register(FinancialAidRequest)

## class_.py

class ProgramCheckItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'program')
admin.site.register(ProgramCheckItem, ProgramCheckItemAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'friendly_times', 'status', 'duration')
    list_display_links = ('title',)
    list_filter = ['status']
    pass
admin.site.register(ClassSection, SectionAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent_program', 'category')
    list_display_links = ('title',)
    search_fields = ['class_info', 'anchor__friendly_name']
admin.site.register(ClassSubject, SubjectAdmin)

admin.site.register(ClassCategories)