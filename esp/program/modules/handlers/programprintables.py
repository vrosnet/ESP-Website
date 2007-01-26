from esp.program.modules.base import ProgramModuleObj, needs_teacher, needs_student, needs_admin, usercheck_usetl
from esp.program.modules import module_ext
from esp.web.data        import render_to_response
from django.contrib.auth.decorators import login_required


class ProgramPrintables(ProgramModuleObj):

    @needs_admin
    def printoptions(self, request, tl, one, two, module, extra, prog):
        """ Display a teacher eg page """
        context = {'module': self}

        return render_to_response(self.baseDir()+'options.html', request, (prog, tl), context)



    @needs_admin
    def teacherschedules(self, request, tl, one, two, module, extra, prog):
        """ generate teacher schedules """

        context = {'module': self     }
        teachers = self.program.teachers()
        teachers.sort()

        scheditems = []

        for teacher in teachers:
            # get list of valid classes
            for cls in [ cls for cls in teacher.getTaughtClasses()
                         if cls.parent_program == self.program
                         and cls.isAccepted()                  ]:
            
                scheditems.append({'name': teacher.name(),
                                   'cls' : cls})

        context['scheditems'] = scheditems
        return render_to_response(self.baseDir()+'teacherschedule.html', request, (prog, tl), context)
        
    @needs_admin
    def studentschedules(self, request, tl, one, two, module, extra, prog):
        """ generate teacher schedules """

        context = {'module': self     }
        students = self.program.students()
        students.sort()

        scheditems = []

        for student in students:
            # get list of valid classes
            for cls in [ cls for cls in student.getEnrolledClasses()
                         if cls.parent_program == self.program
                         and cls.isAccepted()                  ]:
            
                scheditems.append({'name': student.name(),
                                   'cls' : cls})

        context['scheditems'] = scheditems
        return render_to_response(self.baseDir()+'studentschedule.html', request, (prog, tl), context)
        