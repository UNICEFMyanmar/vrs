import pprint
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
import reversion
from birth_registration.autofixtures import F101Fixture
from birth_registration.models import F101
from birth_registration.permissions import get_codename
from certification.models import F103


# class F103Tests(TestCase):
#     fixtures = ('test_user.json', 'test_f101_model_real_correct_data_x_2.json', 'RHC.json')
#
#     def setUp(self):
#         self.factory = RequestFactory()
#
#         self.username = "test"
#         self.password = "test"
#
#         self.user = User.objects.create_user(username=self.username, password=self.password)
#         self.f101 = F101.objects.get(id=235)
#
#     def test_permissions_F103Create(self):
#         url = reverse("F103CreateView", kwargs={'f101': self.f101})
#         redirect_url = reverse("login") + "?next=" + url
#
#         # user not logged in
#         response = self.client.get(url)
#         self.assertRedirects(response, redirect_url)
#
#         # user logged in, but does not have the permission
#         self.assertTrue(self.client.login(username=self.username, password=self.password))
#         response = self.client.get(url)
#         self.assertRedirects(response, redirect_url)
#
#         # got the permission
#         permission = Permission.objects.get(name='Can add Form 103')
#         self.user.user_permissions.add(permission)
#         self.user.save()
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 404)  # no access to f101 object
#
#         permission = Permission.objects.get(codename=get_codename((self.f101.ST_DV, self.f101.DIS, self.f101.TWN)))
#         self.user.user_permissions.add(permission)
#         self.user.save()
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)  # should be ok
#
#     def _test_F103_post_and_reversion(self):
#
#         url = reverse("F103CreateView", kwargs={'f101': self.f101})
#
#         permission = Permission.objects.get(name='Can view Form 103')
#         self.user.user_permissions.add(permission)
#
#         permission = Permission.objects.get(name='Can add Form 103')
#         self.user.user_permissions.add(permission)
#         permission = Permission.objects.get(codename=get_codename((self.f101.ST_DV, self.f101.DIS, self.f101.TWN)))
#         self.user.user_permissions.add(permission)
#         self.user.save()
#
#         self.assertTrue(self.client.login(username=self.username, password=self.password))
#
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#         data = response.context_data['form'].initial
#
#         data['RHC'] = self.f101.RHC_id or ""
#         data['NCZN_M'] = self.f101.NCZN_M or ""
#
#         response = self.client.post(url, data)
#
#         if hasattr(response, 'context_data'):
#             error_message = pprint.pformat(response.context_data['form'].errors, indent=4)
#         else:
#             error_message = ""
#         self.assertEquals(response.status_code, 302, error_message)
#         f103_url = response['Location']
#         f103_id = int(f103_url.split("/")[4])
#         f103 = F103.objects.get(pk=f103_id)
#
#         reversion_qs = reversion.get_for_object(f103)
#
#         self.assertEquals(reversion_qs.count(), 1)
#
#         response = self.client.get(f103_url)
#         self.assertEquals(response.status_code, 200)
#
#         self.assertEquals(reversion_qs.count(), 2)
#
#     def test_F103_post_and_reversion_no_RHC(self):
#         self.f101 = F101.objects.get(id=235)
#         self._test_F103_post_and_reversion()
#
#     def test_F103_post_and_reversion_with_RHC(self):
#         self.f101 = F101.objects.get(id=236)
#         self._test_F103_post_and_reversion()
