from account.entity.login_history import LoginHistory
from account.entity.profile import Profile
from account.repository.profile_repository import ProfileRepository
from account.entity.profile_gender_type import ProfileGenderType
from account.entity.account_role_type import AccountRoleType

from django.utils import timezone

class ProfileRepositoryImpl(ProfileRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def findByEmail(self, email):
        try:
            profile = Profile.objects.get(email=email)
            return profile
        except Profile.DoesNotExist:
            print(f"email로 profile 찾을 수 없음: {email}")
            return None
        except Exception as e:
            print(f"email 중복 검사 중 에러 발생: {e}")
            return None

    def findByNickname(self, nickname):
        try:
            profile = Profile.objects.get(nickname=nickname)
            return profile
        except Profile.DoesNotExist:
            print(f"nickname으로 profile 찾을 수 없음: {nickname}")
            return None
        except Exception as e:
            print(f"nickname 중복 검사 중 에러 발생: {e}")
            return None

    def create(self, nickname, email, password, salt, gender, birthyear, account):
        genderType = ProfileGenderType.objects.get_or_create(gender_type=gender)
        gender = genderType[0]
        profile = Profile.objects.create(
            nickname=nickname,
            email=email,
            password=password,
            salt=salt,
            gender=gender,
            birthyear=birthyear,
            account=account
        )
        return profile
    def findByPassword(self, email,password):
        try:
            email = Profile.objects.get(email=email)
            return email.password == password
        except email.DoesNotExist:
            print('password가 일치하지 않습니다.')
            return None
        except Exception as e:
            print(f"password로 계정 찾는 중 에러 발생: {e}")
            return None

    def findById(self, accountId):
        try:
            profile = Profile.objects.get(account_id=accountId)
            return profile
        except Profile.DoesNotExist:
            print('accountId와 일치하는 계정이 없습니다')
            return None
        except Exception as e:
            print(f"accountId로 계정 찾는 중 에러 발생: {e}")
            return None

