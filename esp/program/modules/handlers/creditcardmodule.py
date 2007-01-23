from esp.program.modules.base import ProgramModuleObj, needs_teacher, needs_student, needs_admin, usercheck_usetl
from esp.program.modules import module_ext
from esp.web.data        import render_to_response
from esp.money.models    import PaymentType, Transaction
        

class CreditCardModule(ProgramModuleObj):
    def extensions(self):
        return [('creditCardInfo', module_ext.CreditCardModuleInfo)]

    def cost(self):
        return '%s.00' % str(self.creditCardInfo.base_cost)

    def isCompleted(self):
        return Transaction.objects.filter(anchor = self.program.anchor,
                                          fbo = self.user).count() > 0

    @usercheck_usetl
    def startpay(self, request, tl, one, two, module, extra, prog):
        context = {}
        context['module'] = self
        context['one'] = one
        context['two'] = two
        context['tl']  = tl
        return render_to_response(self.baseDir() + 'cardstart.html', request, (prog, tl), context)

    @usercheck_usetl
    def paynow(self, request, tl, one, two, module, extra, prog):

        context = {}
        paymenttype = PaymentType.objects.get(description__icontains = 'credit card')
        payment = Transaction()
        payment.anchor = self.program.anchor
        payment.executed = False # have not verified yet...
        payment.fbo = self.user
        payment.payer = self.user
        payment.payment_type = paymenttype
        payment.line_item = 'Credit-card payment for "%s"' % self.program.niceName()
        payment.amount = self.creditCardInfo.base_cost
        payment.save()
        
        self.payment = payment

        yearnow = datetime.now().year
        context['years'] = zip(range(yearnow-2000, yearnow+20-2000),
                               range(yearnow, yearnow+20))
        context['module'] = self
        return render_to_response(self.baseDir() + 'cardpay.html', request, (prog, tl), context)
