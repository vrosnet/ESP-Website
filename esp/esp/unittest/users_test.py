
__author__    = "MIT ESP"
__date__      = "$DATE$"
__rev__       = "$REV$"
__license__   = "GPL v.2"
__copyright__ = """
This file is part of the ESP Web Site
Copyright (c) 2007 MIT ESP

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
from esp.unittest.unittest import TestCase, TestSuite

from esp.unittest.datatree_test import TreeTest
from esp.users.models import UserBit
from esp.datatree.models import GetNode
from django.contrib.auth.models import User

class UserTest(TestCase):
    users = (
        ('test1', 'pass1'),
        ('test2', 'pass2'),
        ('test3', 'pass3'),
        ('Fred', 'none'),
        ('Bob', 'password'),
        ('Joe', 'kc sdklnmawefovsdmlkasdmkfla;wefcvm zkido as;3ear;j a340wwei9f0a'),
        )

    saved_users = []

    def setUp(self):
        """ Create and link ESP users """
        self.saved_users = []

        for u in self.users:
            if User.objects.filter(username=u[0]).count() == 0:
                django_user = User()
                django_user.username = u[0]
                django_user.set_password(u[1])
                django_user.is_staff = False
                django_user.is_superuser = False
                django_user.save()

                """espuser = User()
                espuser.user = django_user
                espuser.save()
            
                self.saved_users.append( [django_user, espuser] )"""
            else:
                print 'Error creating user ' + u[0] + '; user already exists.'

                """possible_users = User.objects.filter(username=u[0])
                if len(possible_users) == 1:
                    django_user = possible_users[0]

                    possible_espusers = User.objects.filter(user__pk=django_user.id)
                    if possible_espusers.count() == 1:
                        espuser = possible_espusers[0]
                        self.saved_users.append( [django_user, espuser] )"""

    def tearDown(self):
        """ Remove our sample users """
        for user_set in self.saved_users:
            user_set[1].delete()
            user_set[0].delete()

        self.saved_users = []
        
class UserBitsTest(UserTest, TreeTest):
    bits = []
    
    def setUp(self):
        super(UserBitsTest, self).setUp()
            
        """ Create an arbitrary set of user bits, based on currently-existing data """
        length = min( len(self.saved_users), len(self.usergrouptree_nodes), len(self.sitetree_nodes))

        for i in range(0,length):
            bit = UserBit()
            bit.user = self.saved_users[i][1]
            bit.qsc = GetNode(self.sitetree_nodes[i])
            bit.verb = GetNode(self.usergrouptree_nodes[i])
            bit.save()
            
            self.bits.append( bit )

        for i in range(0, len(self.saved_users)/2):
            bit = UserBit()
            bit.user = self.saved_users[i][1]
            bit.qsc = GetNode(self.sitetree_nodes[ i % len(self.sitetree_nodes) ] )
            bit.verb = GetNode('V/Subscribe')
            bit.save()

            self.bits.append(bit)
        
    def tearDown(self):
        """ Get rid of the users that we created in setUp() """
        super(UserBitsTest, self).tearDown()

        for bit in self.bits:
            try:
                bit.delete()
            except Exception:
                pass
            
        self.bits = []
        
