# 트위치 뱅온 알림
* 원하는 스트리머들의 뱅온을 알려주는 데스크탑 프로그램입니다.

## 기능
* 원하는 스트리머들이 뱅온시 알림을 보내줍니다.
  * 스트리머 7명 기준 평균 40초 정도의 딜레이
  * 스트리머의 수가 늘어날 수록 딜레이가 길어집니다.
* 프로그램 최초 실행 시, 현재 방송중인 스트리머에 대해서도 알림을 보내줍니다.
* 알림을 클릭할 시 해당 방송으로 이동합니다.

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162577002-1f709fb9-e9b0-401b-b779-d6b1de156b91.png" width="30%"/></p>

## 실행방법
### 프로그램 다운로드
1. 우측의 'Releases'를 눌러 Assets의 'twitchAlarm.zip' 파일을 다운받은 후, 압축을 풀어줍니다.

![image](https://user-images.githubusercontent.com/47859342/162577766-573a157b-c5bc-4c03-a2e3-6903d9bde342.png)

### TwitchAPI 설정
1. 본 프로그램은 TwitchAPI를 사용하기 때문에, 이를 위한 사전작업이 필요합니다.
2. [Twitch 개발자 홈페이지](https://dev.twitch.tv/)에 접속합니다.
3. 우측 상단 'Log in with Twitch'를 눌러 로그인합니다. 

<img width="1920" alt="스크린샷 2022-04-09 21 21 45" src="https://user-images.githubusercontent.com/47859342/162573980-4dd8f436-a948-4550-9dea-d995d49729fd.png">

4. 로그인에 성공하면 이전과 같은 위치에 있는 'Your Console' 버튼을 눌러 콘솔에 접속합니다.

<img width="1920" alt="스크린샷 2022-04-09 21 23 29" src="https://user-images.githubusercontent.com/47859342/162574017-37902e89-e66d-47a2-a975-b56d01bc72a5.png">

5. 우측의 'Applications' 탭의 'Register your application' 버튼을 클릭합니다.

<img width="1920" alt="스크린샷 2022-04-09 21 24 42" src="https://user-images.githubusercontent.com/47859342/162574058-c69269db-44c0-4b0c-9960-168cfc39405c.png">

6. 'Name'에는 아무런 이름이나 적어도 무방합니다.(이름 중복은 안됨)

<img width="1920" alt="스크린샷 2022-04-09 21 27 14" src="https://user-images.githubusercontent.com/47859342/162574138-c032f26c-01af-4f79-8355-7a2eaa4fc3c4.png">

7. 'OAuth Redirect URLs'에 'https://localhost'를 적은 후, 'Add' 버튼을 눌러줍니다.

<img width="1920" alt="스크린샷 2022-04-09 21 31 30" src="https://user-images.githubusercontent.com/47859342/162574274-66148eb3-ac7e-4b1a-b62e-d70d91e5ef9e.png">

8. 'Category'는 아무거나 설정해줍니다

<img width="1920" alt="스크린샷 2022-04-09 21 32 29" src="https://user-images.githubusercontent.com/47859342/162574298-579dfcd0-c1a3-499a-aadd-b20d8746edde.png">

9. 'Create' 버튼을 누르면 설정이 완료되며, 'Manage' 버튼을 눌러 확인가능합니다.

<img width="1920" alt="스크린샷 2022-04-09 21 33 14" src="https://user-images.githubusercontent.com/47859342/162574318-8200490b-9073-4642-9d43-f60692fc8516.png">

10. 가장 아래 'Client Secret'의 'New Secret'을 눌러주고, 알림창이 뜨면 확인을 눌러줍니다. 발급받은 client id와 client secret을 확인합니다.
* Client Secret은 이 창을 나가면 다시 확인할 수 없고, 재발급만 가능하므로 따로 적어두는 것이 좋습니다.

<img width="1920" alt="스크린샷 2022-04-09 21 34 38" src="https://user-images.githubusercontent.com/47859342/162574462-67d53aac-e09c-41fe-bc7c-fd015ed2e59d.png">

11. 윈도우 버튼 옆의 검색창을 눌러 '시스템 환경 변수 편집'을 눌러줍니다.

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162573359-9a0ef038-305e-42e6-8a89-bf12e0b26c52.png" width="50%"/></p>

12. 가장 아래의 '환경 변수'를 눌러줍니다.

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162573384-64be57d2-a9bb-40a1-985c-2f3204df7427.png" width="50%"/></p>

13. 가장 위의 '사용자 변수'에서 '새로 만들기'를 눌러줍니다.

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162573462-2b310660-acd8-471f-be7b-9b8d3b9cd03f.png" width="50%"/></p>

14. 변수 이름을 'client_id', 변수 값을 발급받은 Client id로 입력한 후 확인을 눌러줍니다.

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162573479-cf722349-1d92-4b98-b03e-5e8cdae17349.png" width="50%"/></p>

15. 똑같이 변수 이름을 'client_secret', 변수 값을 발급받은 Client secret으로 입력한 후 확인을 눌러줍니다.

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162573496-3176bce1-138e-41ab-b420-68536c4fa1c1.png" width="50%"/></p>

### 프로그램 실행
1. 다운받은 프로그램 폴더를 열어줍니다.
2. 폴더 내 'channelList.txt' 파일에 원하는 스트리머들의 트위치 아이디를 적어 뱅온알림을 받을 수 있습니다. (더 많은 아이디를 입력할 수록 뱅온알림이 오는 시간이 길어집니다.)

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162573526-e8fe816d-6671-416e-a458-7689a06ba27d.png" width="30%"/></p>

3. 'main.exe'를 더블클릭하여 프로그램을 실행합니다.

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162575110-d39968dc-dd6c-4613-a33a-a1811f68872b.png" width="80%"/></p>

* 아래와 같은 창이 뜰 수 있는데, '추가 정보'를 눌러 실행해주시면 됩니다. 프로그램의 코드는 깃허브에 공개되어 있고, 악성코드는 없으니 안심하셔도 됩니다. 

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162576611-323adb09-0639-4010-b586-8abde57caed9.png" width="80%"/></p>

* 마우스 우클릭하여 바로가기를 생성한 후, 바탕화면으로 옮기면 편리하게 사용하실 수 있습니다.

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162577297-4b07d8b2-f3a8-4f33-88e5-646806e5ceaa.png" width="20%"/></p>

* 다음 그림과 같이 터미널창을 클릭할 경우 좌측에 '선택'이라고 뜨는데, 이럴 경우 프로그램이 정상적으로 실행되지 않을 수 있습니다. '선택'이 뜨지 않음을 확인하여 주시고, 만약 뜰 경우, ESC 키를 누르거나 다른 창을 누르면 해결됩니다.

<p align="center"><img src="https://user-images.githubusercontent.com/47859342/162575034-7dcd1c86-7671-4f43-a2d2-a58a99f7115c.png" width="70%"/></p>

