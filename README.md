#### 게시판 CRUD API

##### 기술환경
- Django 3.2.8
- python 3.8

##### 구현 기능(구현 방법과 이유, 실행 방법)
- 회원가입
  - 구현 방법: CBV인 FormView 사용
  - 이유: 커스텀한 폼을 사용하고, form_valid() 메서드로 폼을 컨트롤하기 쉬운 뷰이기 때문
  - 실행 방법: http://localhost:8000/users/login/

- 로그인
  - 구현 방법: CBV인 FormView 사용
  - 이유: 커스텀한 폼을 사용하고, form_valid() 메서드로 폼을 컨트롤하기 쉬운 뷰이기 때문
  - 실행 방법: http://localhost:8000/users/signup/

- 로그아웃
  - 구현 방법: FBV 사용
  - 이유: 장고의 Auth에서 제공하는 logout를 사용하면 간단하게 구현할 수 있기 때문
  - 실행 방법: http://localhost:8000/users/logout/

- 유저 인가 기능 
  - LogginedOnlyView
    - 구현 방법: 유저 앱 내부에 믹스인으로 만들어서 재활용함
    - 이유: 글 생성, 글 수정 등 로그인 된 유저만 접근 가능한 기능이 많기 때문에 재활용할 수 있는 믹스인을 선택함. 내부에서는 LoginRequiredMixin상속받아 구현함   
    - 실행 방법: BoardCreateView, BoardUpdateView에 상속받아서 사용함

  - LoggedOutOnlyView
    - 구현 방법: 유저 앱 내부에 믹스인으로 만들어서 재활용함
    - 이유: 로그아웃된 사람만 로그인할 수 있고, 로그인된 유저가 로그인페이지로 접근 시 홈으로 리다이렉트됨. 내부에서는 UserPassesTestMixin 상속받아 구현함   
    - 실행 방법: LoginView에 상속받아 사용함

  - @login_required
    - 구현 방법: 장고 Auth의 데코레이터를 임포트하여 사용
    - 이유: LogginedOnlyView는 CBV에서만 사용가능하기 때문에 FBV로 구현시 사용할 수 있음
    - 실행 방법: delete_board()함수 바로 위에서 호출하여 사용함

- 글 목록 확인
  - 구현 방법: CBV인 ListView 사용
  - 이유: 내부 속성으로 paginated_by, paginate_orphans를 제공하여 pagination을 구현하기 편리함, 그 외 ordering 등 다양한 속성을 사용할 수 있음
  - 실행 방법: http://localhost:8000/

- 글 작성
  - 구현 방법: CBV인 FormView 사용
  - 이유: 커스텀한 폼을 사용하고 폼 객체를 저장하는 과정을 인터셉트 할 수 있기 때문. 폼 내부 save()메서드에서 commit=False 한 후, form_valid() 메서드에서 FK로 엮인 writer 필드에 객체를 할당하여 객체 생성함 
  - 실행 방법: http://localhost:8000/boards/create/

- 글 확인(디테일)
  - 구현 방법: CBV인 DetailView 사용
  - 이유: 파라미터로 pk를 받지 않아도 뷰 안에서 제공하기 때문에 디테일 페이지를 구현할 때 용이함  
  - 실행 방법: http://localhost:8000/boards/detail/16

- 글 수정
  - 구현 방법: CBV인 UpdateView 사용
  - 이유: 내부에 fields 속성을 사용하여 모델에서 수정하고 싶은 필드만 선택하여 수정이 용이하기 때문, 또한, get_object메서드를 사용하여 글 작성자가 아닌 유저가 접근할 때 차단하기 용이함
  - 실행 방법: http://localhost:8000/boards/edit/16

- 글 삭제
  - 구현 방법: FBV 사용
  - 이유: 장고에서 제공하는 뷰의 기능을 사용하는 것이 아니라, 수정하려는 객체가 존재하는지, 로그인한 유저가 해당 글을 삭제하는게 맞는지 확인하는 로직을 작성하기에 FBV가 편하기 때문
  - 실행 방법: http://localhost:8000/boards/delete/16

##### API 명세
- 헤더, 파라미터, 바디, response param, response code, message 등 추가 필요
- https://www.notion.so/f6c5b5d7ad954d28a0618655ed5dfe12?v=dae55b3c305c47b99f568232035f9efa