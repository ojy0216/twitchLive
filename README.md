# 트위치 뱅온 알림
* 원하는 스트리머들의 뱅온을 알려주는 데스크탑 프로그램입니다.

## 실행방법
### 프로그램 다운로드
1. 우측의 'Releases'를 눌러 각자의 운영체제에 맞는 파일을 다운받은 후, 압축을 풀어줍니다.

### TwitchAPI 설정
1. 본 프로그램은 TwitchAPI를 사용하기 때문에, 이를 위한 사전작업이 필요합니다.
1. [Twitch 개발자 홈페이지](https://dev.twitch.tv/)에 접속합니다.
1. 우측 상단 'Log in with Twitch'를 눌러 로그인합니다. 
1. 로그인에 성공하면 이전과 같은 위치에 있는 'Console' 버튼을 눌러 콘솔에 접속합니다.
1. 우측의 'Applications' 탭의 'Register your application' 버튼을 클릭합니다.
1. 'Name'에는 아무런 이름이나 적어도 무방합니다.
1. 'OAuth Redirect URLs'에 'https://localhost'를 적은 후, 'Add' 버튼을 눌러줍니다.
1. 'Category'는 아무거나 설정해줍니다.
1. 'Create' 버튼을 누르면 설정이 완료되며, 'Manage' 버튼을 눌러 확인가능합니다.
1. 가장 아래 'Client Secret'의 'New Secret'을 눌러주고, 알림창이 뜨면 확인을 눌러줍니다.
1. Client Secret은 이 창을 나가면 다시 확인할 수 없고, 재발급만 가능하므로 따로 적어두는 것이 좋습니다.

#### Windows 사용자의 경우
13. 

#### MacOS 사용자의 경우
13. 'Command + Space'를 눌러 Spotlight 검색에서 '터미널'을 입력해 실행합니다.
1. 터미널에서 'open ~/.zshrc'를 입력합니다.
1. 텍스트 편집기에 다음과 같이 앞서 발급받은 client_id와 client_secret을 입력해줍니다. (CLIENT_ID, CLIENT_SECRET 위치에 본인이 발급받은 것 입력)
```
export client_id='CLIENT_ID'
export client_secret='CLIENT_SECRET'
```
16. 입력을 완료했으면 텍스트 편집기와 터미널을 모두 종료해줍니다. (단순히 종료하지 말고 Dock에서 오른쪽 마우스 클릭하여 완전히 종료해주세요.)

### 프로그램 실행
1. 다운받은 프로그램 폴더를 열어줍니다.
1. 'channelList.txt' 파일에 원하는 스트리머들의 트위치 아이디를 적어 뱅온알림을 받을 수 있습니다. (더 많은 아이디를 입력할 수록 뱅온알림이 오는 시간이 길어집니다.)

#### Windows 사용자의 경우

#### MacOS 사용자의 경우
1. Unix 실행파일 'main'을 더블클릭하여 프로그램을 실행합니다.