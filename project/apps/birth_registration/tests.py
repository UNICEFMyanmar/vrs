# import json
# import os
# import random
#
# from dateutil.parser import parse
# from django.core.urlresolvers import reverse
# from django.contrib.auth.models import User, Permission
# from django.test import TestCase, RequestFactory
# from django.utils import timezone
# import reversion
#
# from birth_registration.autofixtures import generate_triple
# from birth_registration.codes import URBAN, RURAL, ANY_HOSPITAL_CODE, Sub_code_No_Dictionary
# from birth_registration.models import F101, F201
# from birth_registration.permissions import get_codename
#
#
# class BaseSetup(TestCase):
#     username = "test"
#     password = "test"
#
#     def get_location_permission(self):
#         return Permission.objects.get(
#             codename=get_codename(
#                 (
#                     getattr(self.f101, self.ST_DV),
#                     getattr(self.f101, self.DIS),
#                     getattr(self.f101, self.TWN)
#                 )
#             )
#         )
#
#     def reset_user_form_permissions(self):
#
#         for permission in self.user.user_permissions.all():
#             self.user.user_permissions.remove(permission)
#
#         permission = Permission.objects.get(codename='view_%s' % self.model_name)
#         self.user.user_permissions.add(permission)
#         permission = Permission.objects.get(codename='add_%s' % self.model_name)
#         self.user.user_permissions.add(permission)
#         permission = Permission.objects.get(codename='change_%s' % self.model_name)
#         self.user.user_permissions.add(permission)
#         self.user.save()
#
#     def setUp(self):
#
#         self.model_name = self.model._meta.model_name
#         self.factory = RequestFactory()
#
#         if not User.objects.filter(username=self.username).exists():
#             self.user = User.objects.create_user(username=self.username, password=self.password)
#         else:
#             self.user = User.objects.get(username=self.username)
#
#         self.assertTrue(self.client.login(username=self.username,
#                                           password=self.password))
#
#         fixture = os.path.join(os.path.join(os.path.dirname(__file__), 'fixtures'),
#                                self.form_fixture)
#
#         with open(fixture) as fp:
#             self.data = json.load(fp)
#
#
# class BaseTest(BaseSetup):
#     model = F101
#     object_id = 236
#
#     ST_DV = 'ST_DV'
#     DIS = 'DIS'
#     TWN = 'TWN'
#     NR_AREA = 'NR_AREA'
#
#     F101List = "F101List"
#     F101Detail = "F101Detail"
#     F101Edit = "F101Edit"
#     F101Delete = "F101Delete"
#
#     form_fixture = 'test_f101_form_real_correct_data.json'
#     fixtures = ('test_user.json', 'test_f101_model_real_correct_data_x_2.json', 'RHC.json')
#
#     def setUp(self):
#         super(BaseTest, self).setUp()
#         self.reset_user_form_permissions()
#         self.f101 = self.model.objects.get(id=self.object_id)
#         self.user.user_permissions.add(self.get_location_permission())
#         self.user.save()
#         self.url_edit = reverse(self.F101Edit, kwargs={'pk': self.f101.pk})
#         self.url_detail = reverse(self.F101Detail, kwargs={'pk': self.f101.pk})
#
#     def test_location_form_access(self):
#         self.reset_user_form_permissions()
#
#         response = self.client.get(self.url_detail)
#         self.assertEquals(response.status_code, 404)
#
#         response = self.client.get(self.url_edit)
#         self.assertEquals(response.status_code, 404)
#
#         self.user.user_permissions.add(self.get_location_permission())
#
#         response = self.client.get(self.url_detail)
#         self.assertEquals(response.status_code, 200)
#
#     def test_location_validation(self):
#         comment = 'testing now'
#         self.data['comment'] = comment
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertRedirects(response, self.url_detail)
#
#         st_dv = self.data[self.ST_DV]
#         while self.data[self.ST_DV] == st_dv:
#             (self.data[self.ST_DV], self.data[self.DIS], self.data[self.TWN]) = generate_triple()
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertEquals(response.status_code, 200)
#         self.assertFormError(response, 'form', '', u'You are not allowed to create or edit entries for this region')
#
#         (self.data[self.ST_DV], self.data[self.DIS], self.data[self.TWN]) = ("", "", "")
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertEquals(response.status_code, 200)
#         self.assertFormError(response, 'form', '', u'You are not allowed to create or edit entries for this region')
#
#
#     def test_RHC_or_CIR(self):
#
#         def random_TWN():
#             return random.choice(Sub_code_No_Dictionary.keys())
#
#         def random_CIR(twn=None):
#             cir = ""
#             while not cir or cir == ANY_HOSPITAL_CODE:
#                 if not twn:
#                     twn = random_TWN()
#                 cir = Sub_code_No_Dictionary[twn]
#                 if not type(cir) == int:
#                     cir = random.choice(cir)
#
#             return cir
#
#         comment = 'testing now'
#         self.data['comment'] = comment
#
#         real_RHC = self.data['RHC']
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertRedirects(response, self.url_detail)
#
#         self.data['RHC'] = 1
#         self.data['CIR'] = ""
#         self.data[self.NR_AREA] = URBAN
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertEquals(response.status_code, 200)
#         self.assertFormError(response, 'form', 'RHC', u'You can not use this field for urban areas')
#
#         self.data['RHC'] = 1
#         self.data['CIR'] = ""
#         self.data[self.NR_AREA] = RURAL
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertFormError(response, 'form', 'RHC', u'This RHC belongs to another township')
#
#         self.data['CIR'] = ""
#         self.data[self.NR_AREA] = RURAL
#         self.data['RHC'] = real_RHC
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertRedirects(response, self.url_detail)
#
#         self.data[self.NR_AREA] = RURAL
#         self.data['CIR'] = random_CIR()
#         self.data['RHC'] = real_RHC
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertFormError(response, 'form', 'CIR',
#                              u'Please check the code: looks like it should be %s' % ANY_HOSPITAL_CODE)
#
#
#         while self.data[self.TWN] not in Sub_code_No_Dictionary.keys():
#             (self.data[self.ST_DV], self.data[self.DIS], self.data[self.TWN]) = generate_triple()
#
#         twn = self.data[self.TWN]
#         while twn == self.data[self.TWN]:
#             twn = random_TWN()
#
#         self.data[self.NR_AREA] = URBAN
#         self.data['CIR'] = random_CIR(twn)
#         self.data['RHC'] = ""
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertFormError(response, 'form', 'CIR',
#                              u'This hospital belongs to another township or town')
#
#
#     def test_f101_reversion_on_get(self):
#         url = reverse(self.F101Detail, kwargs={'pk': self.f101.pk})
#
#         reversion_qs = reversion.get_for_object(
#             self.f101)
#
#         revisions = reversion_qs.count()
#
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#
#         self.assertEquals(reversion_qs.count(), revisions + 1)
#
#     def test_f101_reversion_and_updated_at_on_post(self):
#         updated_at = self.f101.updated_at
#
#         reversion_qs = reversion.get_for_object(self.f101)
#         revisions = reversion_qs.count()
#
#         response = self.client.get(self.url_edit)
#         self.assertEquals(response.status_code, 200)
#
#         self.assertEquals(updated_at, self.f101.updated_at)
#
#         self.assertEquals(reversion_qs.count(), revisions + 1)
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertEquals(response.status_code, 200)  # we need a comment
#
#         self.assertFormError(response, 'form', 'comment', 'This field is required.')  # yes, we do
#
#         comment = 'testing now'
#         self.data['comment'] = comment
#
#         response = self.client.post(self.url_edit, self.data)
#         self.assertRedirects(response, self.url_detail)
#
#         self.assertEquals(reversion_qs.count(), revisions + 3)
#         self.assertIn(comment, reversion_qs.all()[1].revision.comment)
#
#         self.f101.refresh_from_db()
#         self.assertNotEquals(updated_at, self.f101.updated_at)
#         self.assertTrue((self.f101.updated_at - timezone.now()).total_seconds() < 1)
#
#         # todo: check updated_at on form creation for both F101 and F201
#
#     def test_delete_permissions(self):
#         url = reverse(self.F101Delete, kwargs={'pk': self.f101.id})
#
#         response = self.client.post(url)
#
#         self.assertTrue(reverse('django.contrib.auth.views.login') in response['Location'])
#
#         self.f101.refresh_from_db()
#         self.assertFalse(self.f101.deleted)
#
#         permission = Permission.objects.get(codename='change_%s' % self.model_name)
#         self.user.user_permissions.add(permission)
#         self.user.save()
#         response = self.client.post(url)
#
#         self.assertTrue(reverse('django.contrib.auth.views.login') in response['Location'])
#
#         self.f101.refresh_from_db()
#         self.assertFalse(self.f101.deleted)
#
#         permission = Permission.objects.get(codename='delete_%s' % self.model_name)
#         self.user.user_permissions.add(permission)
#         self.user.save()
#         response = self.client.post(url)
#
#         self.assertEqual(response.status_code, 200)
#
#         self.f101.refresh_from_db()
#         self.assertFalse(self.f101.deleted)
#
#         self.data['comment'] = 'testing'
#         response = self.client.post(url, self.data)
#
#         self.assertRedirects(response, reverse(self.F101List))
#
#         self.f101.refresh_from_db()
#         self.assertTrue(self.f101.deleted)
#
#
# ###############################################################################################
#
# # class F201_Base_test(BaseTest):
# #     model = F201
# #
# #     form_fixture = 'test_f201_form_real_correct_data.json'
# #     fixtures = ('test_user.json', 'test_f201_model_real_correct_data.json', 'RHC.json')
# #     object_id = 9
# #
# #     F101Detail = "F201Detail"
# #     F101Edit = "F201Edit"
# #     F101Delete = "F201Delete"
# #     F101List = "F201List"
# #
# #     ST_DV = 'NNRT'
# #     DIS = 'NNRT1'
# #     TWN = 'NNST'
# #     NR_AREA = 'NNVD'
#
#
# # class Test101RealData(BaseSetup):
# #     fixtures = ('test_user.json', 'test_f201_model_real_correct_data.json', 'RHC.json')
# #     form_fixture = 'test_data_real_database.json'
# #     model = F101
# #     F101Add = "F101Create"
# #     username = 'kostik'
# #     password = '123'
# #
# #     def setUp(self):
# #         super(Test101RealData, self).setUp()
# #
# #         self.assertTrue(self.client.login(username=self.username,
# #                                           password=self.password))
# #
# #         self.url_add = reverse(self.F101Add)
# #         response = self.client.get(self.url_add)
# #         self.form_fields = response.context['form'].fields
# #
# #     def form_post(self, obj):
# #         form_data = {}
# #         for field, value in obj['fields'].iteritems():
# #             if self.form_fields.has_key(field):
# #                 if "Date" in field:
# #                     try:
# #                         value = parse(value).strftime("%d%m%Y")
# #                     except ValueError:
# #                         pass
# #                 if value:
# #                     form_data[field] = value
# #                 else:
# #                     form_data[field] = ""
# #
# #         response = self.client.post(self.url_add, form_data)
# #         if response.status_code == 200:
# #             return obj['pk']
# #         return None
# #
# #     def test_real_data(self):
# #
# #         fixture = os.path.join(os.path.join(os.path.dirname(__file__), 'fixtures'),
# #                                self.form_fixture)
# #
# #         with open(fixture) as fp:
# #             self.data = json.load(fp)
# #
# #         errors = []
# #         for obj in self.data:
# #             error_pk = self.form_post(obj)
# #             if error_pk:
# #                 errors.append(error_pk)
# #         self.assertListEqual([9, 10, 11, 12, 13, 16, 19, 21, 22, 26, 107, 122], errors)
#
