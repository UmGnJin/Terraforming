from tkinter import*
import time
from tkinter import messagebox
import random
from tkinter.simpledialog import*
## 변수들의 목록
daycountinfo=1

## 전문 인력
sch, schpow=0, 1
wor, worpow=0, 1
core, corefrag=0, 0

##게임 시작 확인
start, tut=1, 1
##각 창의 튜토리얼
techtut, labtut, armtut, herotut, combattut=1, 1, 1, 1, 1
bosscount=1
## 각 기술의 기술력 요구량

##기술의 티어
tier, labortier=1, 1

##티어 1
laserbeam, darkmatter, megaengine, buildskill=20, 20, 20, 50
##티어1 완료여부
laserbeamok, darkmatterok, megaengineok, buildskillok=0, 0, 0, 0
##티어 2
graphenearmor, uv, poison, ai, gigaengine, firststrike=50, 50, 50, 50, 50, 50
##티어 2 완료 여부
graphenearmorok, uvok, poisonok, aiok, gigaengineok, firststrikeok=0, 0, 0, 0, 0, 0

##건설 관련 변수

##군사 건물
barracks, barracksok=100, 0
fortress, fortressok=300, 0

##연구 건물
dmlab, dmlabok=50, 0
pslab, pslabok=450, 0

##방어 건물
bunker, bunkernum=40, 0
## 기타 변수
trainnum=0
recycle, recyclenum=200, 0

##군사 관련 변수

##보병
walker, walkerpower, walkerdef=0, 5, 1
##포병
mortar, mortarpower=0, 16
##기병
crow, crowpower, crowspeed=0, 4, 3
fscount, fs=1, 1
##자원량
goldamount, lpamount, apamount, tpamount, day, people, technology=0, 0, 0, 0, 1, 250, 0
apamount=people+mortar*mortarpower+walker*walkerpower+crow*crowpower+fortressok*50
##영웅 스탯
Str, Dex, Int= 10, 10, 10
##자원의 변화
goldupdown, tpupdown, lpupdown=0, 0+Int+sch*schpow+core*15, 0+wor*worpow+corefrag*5
score=0
fleeok=0
##몬스터들


ailen, beast, golem=0, 0, 0

ailenmaxhp, ailencurhp, ailenatk, ailenskill=500, 500, 50, 3
beastmaxhp, beastcurhp, beastatk, beastskill=400, 400, 150, 2
golemmaxhp, golemcurhp, golematk, golemskill=1200, 1200, 150, 1
shaman=1
shamanmaxhp, shamancurhp, shamanatk=3000, 3000, 130
alive=1
## 점수 시스템
score=0

##함수 함수------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def DoubleFunc(func1, func2, func3=None):
    func1
    func2
    func3
##게임 오버
def GameOver():
    global goldamount
    gameover=Tk()
    gameover.geometry('400x200+300+250')
    gameover.title("게임 오버\n 당신의 점수 : %d"%goldamount)
    frame=Frame(gameover)
    frame.pack(fill=BOTH)
    confirm=Button(frame, text="확인", command=quit)
    confirm.pack(side=BOTTOM, pady=10)
##튜토리얼
def Tutorial():
    messagebox.showinfo("튜토리얼", "반갑습니다 지도자님. 앞으로 기초적인 목적을 설명할 부관입니다.")
    a=askinteger("부관", "튜토리얼을 진행하시겠습니까? 그렇다면 1을, 아니면 다른 숫자를 입력해 주세요.")
    if a!=1:
        messagebox.showinfo("튜토리얼", "우선 개척지를 마련했으니 후발대가 올 1달동안 이곳에서 생존하면 됩니다.")
        messagebox.showinfo("튜토리얼", "최상단에서는 메뉴를, 바로 아래의 노란색 줄에서는 자원 표시창이 있습니다.")
        messagebox.showinfo("튜토리얼",  "우측의 초록색 공간에서는 여러 기능을 사용하기 위한 공간으로 이동이 가능합니다.")
        messagebox.showinfo("튜토리얼",  "하얀 공간은 게임의 맵이 제공될 예정입니다.")
        messagebox.showinfo("튜토리얼",  "위쪽 메뉴에서는 게임 종료나 설정 등의 기능들을 이용하실 수 있습니다.")
        messagebox.showinfo("튜토리얼", "튜토리얼을 다시 확인하시려면 메뉴에서 튜토리얼 버튼을 클릭해 주세요.")
        messagebox.showinfo("튜토리얼", "세부 창 내에서 버튼을 우클릭하면 상세 설명이 있을 수도 있으니 참고하세요.")
        global daycountinfo
        if daycountinfo==1:
            messagebox.showinfo("튜토리얼", "아, 참고로 알아본 것인데, 생명체로 추정되는 것들이 이곳으로 다가오고 있다고 합니다. 3일째에는 이곳에 다다른다고 하네요.")
##날짜 변경
def NextDay():
    global day, daycountinfo
    global goldamount, goldupdown
    global tpamount, tpupdown
    global lpupdown, lpamount
    global ailen, ailencurhp, ailenmaxhp, ailenatk
    global beast, beastcurhp, beastmaxhp, beastatk
    global golem, golemcurhp, golemmaxhp, golematk
    ##하루가 끝나며 발생하는 이벤트 목록
    day=day+1
    daycountinfo=1
    goldamount+=goldupdown
    tpamount+=tpupdown
    lpamount+=lpupdown
        
    if day%3==0:
        ailen=1
        ailenmaxhp, ailencurhp, ailenatk=500, 500, 50
    if day%5==0:
        beast=1
        beastmaxhp, beastcurhp, beastatk=400, 400, 150
    if day%10==0:
        golem=1
        golemmaxhp, golemcurhp, golematk=1200, 1200, 130

    main.destroy()    
##기술창------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def TechTut():
    messagebox.showinfo("기술창 튜토리얼", "반갑습니다. 연구소장입니다.")
    a=askinteger("연구소장", "이미 아신다면 1, 아니면 다른 숫자를 입력하시면 됩니다.")
    if a!=1:
        messagebox.showinfo("기술창 튜토리얼", "여기서는 우리 세력에게 필요한 연구 자료들을 모을 수 있어요.")
        messagebox.showinfo("기술창 튜토리얼", "위쪽에서 연구원을 배치해서 연구 자료들을 모으시면 됩니다.")
        messagebox.showinfo("기술창 튜토리얼", "연구 자료들이 모이면 기술을 연구할 수 있습니다.")
        messagebox.showinfo("기술창 튜토리얼", "기술들 옆에 쓰여 있는 숫자들만큼의 기술력이 필요하죠.")
        messagebox.showinfo("기술창 튜토리얼", "연구 가능한 기술들의 버튼이 활성화되었을 때 클릭해서 기술 연구를 하시면 됩니다.")
        messagebox.showinfo("기술창 튜토리얼", "연구가 완료된 기술들은 즉시 효과가 발동되고, 버튼은 파란색으로 비활성화됩니다.")
        messagebox.showinfo("기술창 튜토리얼", "설명을 다시 한 번 듣고 싶으시다면 도움말 버튼을 클릭해주세요.")
def TechWindow():
    main.destroy()
    global techtut, tpamount, tpupdown, sch
    
    tech=Tk()
    tech.overrideredirect(True)
    tech.geometry("{0}x{1}+0+0".format(tech.winfo_screenwidth(), tech.winfo_screenheight()))
    functions=Frame(tech, height=100)
    functions.pack(side=BOTTOM, fill=X)
    back=Button(functions, text="닫기", font=("맑은 고딕", 20), bg="red", command=tech.destroy)
    back.pack(side=RIGHT, padx=50, pady=10)
    helpbtn=Button(functions, text="도움말", font=("맑은 고딕", 20), command=lambda: TechTut())
    helpbtn.pack(side= RIGHT, padx=50, pady=10)
    
    frame=Frame(tech, height=100, bg="white")
    frame.pack(side=TOP, fill=X)
    text1=Label(frame, text="연구원 배치", font=("맑은 고딕", 15),  bg="white")
    text1.pack(side=LEFT, padx=5, pady=5)
    upbutton=Button(frame, text="배치 인원수 결정", font=("맑은 고딕", 15),  command=lambda: TrainSch())
    upbutton.pack(side=LEFT)
    text2=Label(frame, text="연구원 감축", font=("맑은 고딕", 15),  bg="white")
    text2.pack(side=LEFT, padx=5, pady=5)
    downbutton=Button(frame, text="감축 인원수 결정", font=("맑은 고딕", 15),  command=lambda: TrainSch(2))
    downbutton.pack(side=LEFT)
    curtp=Label(frame, text="현재 연구력 : 턴당%d   현재 연구원 수 : %d명"%(tpupdown, sch), font=("맑은 고딕", 15))
    curtp.pack(side=LEFT)
    
    tech1t=Label(tech, borderwidth=2, relief=SOLID, bg="white")
    tech2t=Label(tech, borderwidth=2, relief=SOLID, bg="white")
    tech3t=Label(tech, borderwidth=2, relief=SOLID, bg="white")
    tech1t.pack(fill=X)
    tech2t.pack(fill=X)
    tech3t.pack(fill=X)

    

    def TechUpOne(k=1):
        global tpupdown, core
        global people
        global sch, Int, schpow
        if k>0:
            if k<=people:
                people-=1*k
                sch+=1*k
                tpupdown=Int+sch*schpow+core*15
                curtp.config(text="현재 연구력 : 턴당%d   현재 연구원 수 : %d명"%(tpupdown, sch))
            elif people<k:
                messagebox.showinfo("자원 부족!", "인구수가 부족합니다.")
        elif k<0:
            if -k<=sch:
                people-=1*k
                sch+=1*k
                tpupdown=Int+sch*schpow+core*15
                curtp.config(text="현재 연구력 : 턴당%d   현재 연구원 수 : %d명"%(tpupdown, sch))
            elif sch<-k:
                messagebox.showinfo("자원 부족!", "연구원 수가 부족합니다.")
    def TrainSch(a=1):
        global tpupdown
        global people
        if a==1:
            trainnum=askinteger('수를 입력하세요', '배치할 연구원 수')
            TechUpOne(trainnum)
        if a==2:
            trainnum=askinteger('수를 입력하세요', '감축할 연구원 수')
            TechUpOne(-trainnum)

            
    def Done(bt):
        bt.config(state=DISABLED, bg="blue")
    def Disable(btn):
        btn.config(state=DISABLED)
    ##기술연구 시스템
    def TestStart(tec, i):
        global tpamount
        global laserbeamok, darkmatterok, megaengineok, buildskillok, labortier
        global graphenearmorok, uvok, poisonok, aiok, firststrikeok, gigaengineok
        global walkerdef, walkerpower, mortarpower, crowpower, crowspeed, fs, labortier
        if tec<=tpamount:
            tpamount-=tec
            tec=0
            messagebox.showinfo("연구 완료!", "연구가 성공적으로 끝났습니다.")
            if i==1:
                laserbeamok=1
            elif i==2:
                darkmatterok=1
            elif i==3:
                megaengineok=1
            elif i==10:
                    buildskillok=1
                    labortier=2
            if tier==2:
                if i==4:
                    graphenearmorok=1
                    walkerdef=2
                elif i==5:
                    uvok=1
                    walkerpower+=2
                elif i==6:
                    poisonok=1
                    mortarpower+=10
                elif i==7:
                    aiok=1
                    crowpower+=1
                    mortarpower+=1
                    walkerpower+=1
                elif i==8:
                    firststrikeok=1
                    crowspeed=5
                elif i==9:
                    gigaengineok=1
                    fs=0
                    
    def Update():
        global laserbeamok, darkmatterok, megaengineok, buildskill, buildskillok
        global graphenearmorok, uvok, aiok, firststrikeok, poisonok, gigaengineok
        if laserbeamok==1:
            Done(btn00)
        elif laserbeam>tpamount:
            Disable(btn00)
        if darkmatterok==1:
            Done(btn01)
        elif darkmatter>tpamount:
            Disable(btn01)
        if megaengineok==1:
            Done(btn02)
        elif megaengine>tpamount:
            Disable(btn02)
        if buildskillok==1:
            Done(btn03)
        elif buildskill>tpamount:
            Disable(btn03)
        if tier==2:
            if graphenearmorok==1:
                Done(btn04)
            elif graphenearmor>tpamount:
                Disable(btn04)
            if uvok==1:
                Done(btn05)
            elif poison>tpamount:
                Disable(btn05)
            if poisonok==1:
                Done(btn06)
            elif poison>tpamount:
                Disable(btn06)
            if aiok==1:
                Done(btn07)
            elif ai>tpamount:
                Disable(btn07)
            if firststrikeok==1:
                Done(btn08)
            elif firststrike>tpamount:
                Disable(btn08)
            if gigaengineok==1:
                Done(btn09)
            elif gigaengine>tpamount:
                Disable(btn09)
                
    def UpdateTech(k):
        if k==0:
            btn00.config(text="레이저 빔(%d)"%(laserbeam))
            Update()
        elif k==1:
            btn01.config(text="암흑 물질(%d)"%(darkmatter))
            Update()
        elif k==2:
            btn02.config(text="메가 엔진(%d)"%(megaengine))
            Update()
        elif k==4:
            btn04.config(text="그래핀 갑주(%d)"%(graphenearmor))
            Update()
        elif k==5:
            btn05.config(text="자외선 레이저(%d)"%(uv))
            Update()
        elif k==6:
            btn06.config(text="맹독 폭탄(%d)"%(poison))
            Update()
        elif k==7:
            btn07.config(text="인공지능 시스템(%d)"%(ai))
            Update()
        elif k==8:
            btn08.config(text="선제 타격(%d)"%(firststrike))
            Update()
        elif k==9:
            btn09.config(text="기가 엔진(%d)"%(gigaengine))
            Update()
        elif k==10:
            btn03.config(text="기초 건축 기술(%d)"%(buildskill))
            Update()

    ##개발할 기술들
    btn00=Button(tech1t, text="레이저 빔(%d)"%(laserbeam), font=("맑은 고딕", 15),  command= lambda: DoubleFunc(TestStart(laserbeam, 1), UpdateTech(0)))
    btn00.pack(side=LEFT, padx=20, pady=5)
    if laserbeamok==1:
        Done(btn00)
    elif laserbeam>tpamount:
        Disable(btn00)
    btn00.bind("<Button-3>", lambda k : messagebox.showinfo("레이저 빔", "레이저 건을 사용하는 보병의 훈련이 가능해집니다."))
    btn01=Button(tech1t, text="암흑 물질(%d)"%(darkmatter), font=("맑은 고딕", 15),  command=lambda: DoubleFunc(TestStart(darkmatter, 2), UpdateTech(1)))
    btn01.pack(side=LEFT, padx=20, pady=5)
    if darkmatterok==1:
        Done(btn01)
    elif darkmatter>tpamount:
        Disable(btn01)
    btn01.bind("<Button-3>", lambda k : messagebox.showinfo("암흑 물질", "암흑 물질 포탄을 개발하여 박격포의 생산이 가능해집니다."))
    btn02=Button(tech1t, text="메가 엔진(%d)"%(megaengine), font=("맑은 고딕", 15),  command=lambda: DoubleFunc(TestStart(megaengine, 3), UpdateTech(2)))
    btn02.pack(side=LEFT, padx=20, pady=5)
    if megaengineok==1:
        Done(btn02)
    elif megaengine>tpamount:
        Disable(btn02)
    btn02.bind("<Button-3>", lambda k : messagebox.showinfo("메가 엔진", "메가 엔진을 쓰는 전투 로봇을 개발하여 까마귀의 훈련이 가능해집니다."))
    
    btn03=Button(tech1t, text="기초 건축 기술(%d)"%buildskill, font=("맑은 고딕", 15), command=lambda: DoubleFunc(TestStart(buildskill, 10), UpdateTech(10)))
    btn03.pack(side=LEFT, padx=20, pady=5)
    if buildskillok==1:
        Done(btn03)
    elif buildskill>tpamount:
        Disable(btn03)
    btn03.bind("<Button-3>", lambda k : messagebox.showinfo("기초 건축 기술", "더 다양한 종류의 건물들이 건설 가능해집니다."))

    global tier
    if tier==2:
        btn04=Button(tech2t, text="그래핀 갑주(%d)"%graphenearmor, font=("맑은 고딕", 15), command=lambda: DoubleFunc(TestStart(graphenearmor,4), UpdateTech(4)))
        btn04.pack(side=LEFT, padx=20, pady=5)
        if graphenearmorok==1:
            Done(btn04)
        elif graphenearmor>tpamount:
            Disable(btn04)
        btn04.bind("<Button-3>", lambda k : messagebox.showinfo("그래핀 갑주", "그래핀을 이용해 만든 보병용 갑옷은 가벼우면서도 튼튼해 보병의 방어력을 1 증가시킵니다. "))
    
        btn05=Button(tech2t, text="자외선 레이저(%d)"%uv, font=("맑은 고딕", 15), command=lambda: DoubleFunc(TestStart(uv,5), UpdateTech(5)))
        btn05.pack(side=LEFT, padx=20, pady=5)
        if uvok==1:
            Done(btn05)
        elif uv>tpamount:
            Disable(btn05)
        btn05.bind("<Button-3>", lambda k : messagebox.showinfo("자외선 레이저", "자외선 근처의 파장을 가진 레이저는 생명체의 세포 구조를 손상시켜 공격력을 2 증진합니다."))
        
        btn06=Button(tech2t, text="맹독 폭탄(%d)"%poison, font=("맑은 고딕", 15), command=lambda: DoubleFunc(TestStart(poison,6), UpdateTech(6)))
        btn06.pack(side=LEFT, padx=20, pady=5)
        if poisonok==1:
            Done(btn06)
        elif poison>tpamount:
            Disable(btn06)
        btn06.bind("<Button-3>", lambda k : messagebox.showinfo("맹독 폭탄", "포탄에 섞인 강력한 독은 빠른 속도로 적의 몸을 잠식해나갑니다. 박격포의 공격력이 10 증가합니다."))
        
        btn07=Button(tech2t, text="인공지능 시스템(%d)"%ai, font=("맑은 고딕", 15), command=lambda: DoubleFunc(TestStart(ai,7), UpdateTech(7)))
        btn07.pack(side=LEFT, padx=20, pady=5)
        if aiok==1:
            Done(btn07)
        elif ai>tpamount:
            Disable(btn07)
        btn07.bind("<Button-3>", lambda k : messagebox.showinfo("인공지능 시스템", "모든 병사들이 상황에 맞게 대처할 수 있는 인공지능 시스템의 지시 하에 움직이게 됩니다. 모든 병사들의 전투력이 1 증가합니다."))

        btn08=Button(tech2t, text="선제 타격(%d)"%firststrike, font=("맑은 고딕", 15), command=lambda: DoubleFunc(TestStart(firststrike,8), UpdateTech(8)))
        btn08.pack(side=LEFT, padx=20, pady=5)
        if firststrikeok==1:
            Done(btn08)
        elif firststrike>tpamount:
            Disable(btn08)
        btn08.bind("<Button-3>", lambda k : messagebox.showinfo("선제 타격", "기병대의 선제 타격 공격력이 2 증가합니다."))

        btn09=Button(tech2t, text="기가 엔진(%d)"%gigaengine, font=("맑은 고딕", 15), command=lambda: DoubleFunc(TestStart(gigaengine,9), UpdateTech(9)))
        btn09.pack(side=LEFT, padx=20, pady=5)
        if gigaengineok==1:
            Done(btn09)
        elif gigaengine>tpamount:
            Disable(btn09)
        btn09.bind("<Button-3>", lambda k : messagebox.showinfo("기가 엔진", "까마귀가 강화되어 매 턴 선제 타격을 가합니다."))
        
    if techtut==1:
        TechTut()
        techtut=0
    
    tech.mainloop()
##작업 관련 함수------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def LabTut():
    messagebox.showinfo("작업창 튜토리얼", "반갑습니다! 작업반장입니다. 간단한 작업 현장 명령에 대해 알려드리죠.")
    a=askinteger("작업반장", "혹시 이미 아시는 내용이면 숫자 1을, 아니면 다른 숫자를 입력하시고 확인 버튼을 누르시면 됩니다.")
    if a!=1:
        messagebox.showinfo("작업창 튜토리얼", "우선 상단에서 노동자를 고용할 수 있습니다. 다들 정착민들이니 급료를 받지는 않습니다.")
        messagebox.showinfo("작업창 튜토리얼", "건물들은 종류에 따라 다른 칸에 나뉘어 있고, 기술 연구 등으로 해금하여 건설할 수 있습니다.")
        messagebox.showinfo("작업창 튜토리얼", "건물들 또한 다른 기술이나 병사 훈련에 필요한 경우가 많으니 참고하세요.")
        messagebox.showinfo("작업창 튜토리얼", "군사력에 소모할 인력이 부족하다면 처음으로 적이 침입하기 전에 방어 건물을 짓는 걸 잊지 마십쇼.")
        messagebox.showinfo("작업창 튜토리얼", "방어 건물은 튼튼한 방어선과 함께할 때 그 진가가 발휘되니, 보병 생산은 필수적입니다.")
        messagebox.showinfo("작업창 튜토리얼", "다시 설명을 듣고 싶으시다면 도움말 버튼으로 찾아주시면 됩니다.")
        
##노동력 변화    

##작업창
def LaborWindow():
    global lpupdown
    global wor, labortier
    main.destroy()
    labor=Tk()
    labor.overrideredirect(True)
    labor.geometry("{0}x{1}+0+0".format(labor.winfo_screenwidth(), labor.winfo_screenheight()))
    functions=Frame(labor, height=100)
    functions.pack(side=BOTTOM, fill=X)
    back=Button(functions, text="닫기", font=("맑은 고딕", 20), bg="red", command=labor.destroy)
    back.pack(side=RIGHT, padx=50, pady=10)
    helpbtn=Button(functions, text="도움말", font=("맑은 고딕", 20), command=lambda: LabTut())
    helpbtn.pack(side= RIGHT, padx=50, pady=10)
    frame=Frame(labor, height=50, bg="white")
    frame.pack(side=TOP, fill=X)
    text1=Label(frame, text="노동자 배치", font=("맑은 고딕", 15),  bg="white")
    text1.pack(side=LEFT, padx=5, pady=5)
    upbutton=Button(frame, text="배치 인원 결정", font=("맑은 고딕", 15),  command=lambda: TrainWor())
    upbutton.pack(side=LEFT)
    text2=Label(frame, text="노동자 감축", font=("맑은 고딕", 15),  bg="white")
    text2.pack(side=LEFT, padx=5, pady=5)
    downbutton=Button(frame, text="감축 인원 결정", font=("맑은 고딕", 15),  command=lambda: TrainWor(1))
    downbutton.pack(side=LEFT)
    curlabor=Label(frame, text="현재 노동력 : 턴당 %d   노동자 수 : %d"%(lpupdown, wor), font=("맑은 고딕", 15))
    curlabor.pack(side=LEFT)
    bdnap=Label(labor, borderwidth=2, relief=SOLID, bg="white")
    bdntp=Label(labor, borderwidth=2, relief=SOLID, bg="white")
    bdnlp=Label(labor, borderwidth=2, relief=SOLID, bg="white")
    bdnpp=Label(labor, borderwidth=2, relief=SOLID, bg="white")
    bdnap.pack(fill=X)
    bdntp.pack(fill=X)
    bdnlp.pack(fill=X)
    bdnpp.pack(fill=X)
    def LaborUpOne(k=1):
        global people, corefrag
        global wor
        global lpupdown
        if k>0:
            if k<=people:
                people-=1*k
                wor+=1*k
                lpupdown=wor*worpow+corefrag*5
                curlabor.config(text="현재 노동력 : 턴당 %d   노동자 수 : %d"%(lpupdown, wor))
            elif people<k:
                messagebox.showinfo("자원 부족!", "인구수가 부족합니다.")
        if k<0:
            if -k<=wor:
                people-=k
                wor+=k
                lpupdown=wor*worpow+corefrag*5
                curlabor.config(text="현재 노동력 : 턴당 %d   노동자 수 : %d"%(lpupdown, wor))
            elif wor<-k:
                messagebox.showinfo("자원 부족!", "노동자 수가 부족합니다.")    
    def TrainWor(a=0):
        if a==0:
            trainnum=askinteger('수를 입력하세요', '배치할 노동자 수')
            LaborUpOne(trainnum)
        elif a==1:
            trainnum=askinteger('수를 입력하세요', '감축할 노동자 수')
            LaborUpOne(-trainnum)   
    def Done(bt):
        bt.config(state=DISABLED, bg="blue")
    def Disable(btn):
        btn.config(state=DISABLED)
        
    ##건설 시스템
    def BuildStart(lab, i):
        global barracksok, dmlabok, bunkernum, tier, recyclenum, schpow, pslabok, fortressok, lpamount
        if lab<=lpamount:
            lpamount-=lab
            lab=0
            messagebox.showinfo("건설 완료!", "작업이 성공적으로 끝났습니다.")
            if i==1:
                barracksok=1
            elif i==2:
                dmlabok=1
                tier=2
                messagebox.showinfo("정보", "이제 2티어 기술들을 연구할 수 있습니다.") 
            elif i==3:
                bunkernum+=1 
            elif i==4:
                fortressok=1
            elif i==5:
                recyclenum+=1
            elif i==6:
                pslabok=1
                schpow=2
    def Update():
        if barracksok==1:
            Done(btn00)
        elif barracks>lpamount:
            Disable(btn00)
        if dmlabok==1:
            Done(btn01)
        elif dmlab>lpamount:
            Disable(btn01)
        if bunker>lpamount:
            Disable(btn02)
        if labortier==2:
            if fortressok==1:
                Done(btn03)
            elif fortress>lpamount:
                Disable(btn03)
            if recycle>lpamount:
                Disable(btn04)
            if pslabok==1:
                Done(btn05)
            elif pslab>lpamount:
                Disable(btn05)
    def UpdateBdn(i):
        if i==0:
            btn00.config(text="병영(%d)"%(barracks))
            Update()
           
        elif i==1:
            btn01.config(text="암흑 물질 연구소(%d)"%(dmlab))
            Update()
           
        elif i==2:
            btn02.config(text="벙커 (%d) (%d개)"%(bunker, bunkernum))
            Update()
           
        elif i==3:
            btn03.config(text="요새(%d)"%fortress)
            Update()
           
        elif i==4:
            btn04.config(text="금속 재활용 공장(%d)"%recycle)
            Update()
           
        elif i==5:
            btn05.config(text="개인 연구실(%d)"%pslab)
            Update()
           
    ##건축 가능한 건물들
    btn00=Button(bdnap, text="병영(%d)"%(barracks), font=("맑은 고딕", 15),  command= lambda: DoubleFunc(BuildStart(barracks, 1), UpdateBdn(0)))
    btn00.pack(side=LEFT, padx=20, pady=5)
    if barracksok==1:
        Done(btn00)
    elif barracks>lpamount:
        Disable(btn00)
    btn00.bind("<Button-3>", lambda k : messagebox.showinfo("병영", "모든 병사들의 전투력이 1 증가합니다."))
    
    btn01=Button(bdntp, text="암흑 물질 연구소(%d)"%(dmlab), font=("맑은 고딕", 15),  command=lambda: DoubleFunc(BuildStart(dmlab, 2), UpdateBdn(1)))
    btn01.pack(side=LEFT, padx=20, pady=5)
    if dmlabok==1:
        Done(btn01)
    elif dmlab>lpamount:
        Disable(btn01)
    btn01.bind("<Button-3>", lambda k : messagebox.showinfo("암흑 물질 연구소", "일부 기술들이 해금되어 연구가 가능해집니다."))
    
    btn02=Button(bdnap, text="벙커 (%d) (%d개)"%(bunker, bunkernum), font=("맑은 고딕", 15),  command=lambda: DoubleFunc(BuildStart(bunker, 3), UpdateBdn(2)))
    btn02.pack(side=LEFT, padx=20, pady=5)
    if bunker>lpamount:
        Disable(btn02)
    btn02.bind("<Button-3>", lambda k : messagebox.showinfo("벙커", "보병들이 안전하게 전투를 유지할 수 있도록 돕습니다."))
    global labtut
    if labtut==1:
        LabTut()
        labtut=0
    if labortier==2:
        btn03=Button(bdnap, text="요새(%d)"%fortress, font=("맑은 고딕", 15),  command=lambda: DoubleFunc(BuildStart(fortress, 4), UpdateBdn(3)))
        btn03.pack(side=LEFT, padx=20, pady=5)
        if fortressok==1:
            Done(btn03)
        if fortress>lpamount:
            Disable(btn03)
        btn03.bind("<Button-3>", lambda k : messagebox.showinfo("요새", "그 자체로도 전투를 수행 가능한 최고의 방어 시설입니다. 최종 전투력에 50을 더합니다. 이 수치는 감소되지 않습니다."))

        btn04=Button(bdnlp, text="금속 재활용 공장(%d) "%recycle, font=("맑은 고딕", 15),  command=lambda: DoubleFunc(BuildStart(recycle, 5), UpdateBdn(4)))
        btn04.pack(side=LEFT, padx=20, pady=5)
        if recycle>lpamount:
            Disable(btn04)
        btn04.bind("<Button-3>", lambda k : messagebox.showinfo("금속 재활용 공장", "쓸만한 재활용 부품들을 재사용해 이윤을 얻습니다. 여유만 된다면 짓도록 상부에서 지시했습니다."))

        btn05=Button(bdnpp, text="개인 연구실(%d) "%pslab, font=("맑은 고딕", 15),  command=lambda: DoubleFunc(BuildStart(pslab, 6), UpdateBdn(5)))
        btn05.pack(side=LEFT, padx=20, pady=5)
        if pslabok==1:
            Done(btn05)
        if pslab>lpamount:
            Disable(btn05)
        btn05.bind("<Button-3>", lambda k : messagebox.showinfo("개인 연구실", "연구진들이 더더욱 연구에 몰두할 환경을 제공합니다. 연구진들의 연구력이 1 증가합니다."))
        
    labor.mainloop()
##타이틀스크린------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def TitleScreen():   
    titlescreen=Tk()
    titlescreen.title("테라포밍")
    titlescreen.overrideredirect(True)
    
    titlescreen.geometry('305x239+500+300')
    
    photo=PhotoImage(file="600.gif")
    frame=Label(titlescreen, width=305, height=239)
    frame.pack(fill=BOTH)
    canvas=Label(frame, width=305, height=200, image=photo)
    canvas.pack()
    start=Button(frame, text="START", command=titlescreen.destroy)
    start.pack(pady=5, side=LEFT)
    label=Label(frame, text="TERRAFORMING")
    label.pack(side=LEFT)
    quitbtn=Button(frame, text="QUIT", command=quit)
    quitbtn.pack(pady=5, side=LEFT)
    titlescreen.mainloop()    
##군사창------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ArmTut():
    messagebox.showinfo("군사창 튜토리얼", "반갑습니다. 훈련소장입니다.")
    a=askinteger("훈련소장", "이미 아시는 내용이면 1번, 아니면 다른 숫자를 입력 후 확인 버튼을 눌러 주십시오.")
    if a!=1:
        messagebox.showinfo("군사창 튜토리얼", "사실 원시적인 환경이라면, 기본적으로 시민들이 가지고 있는 무기들로도 충분히 자기 보호가 가능합니다.")
        messagebox.showinfo("군사창 튜토리얼", "다만, 이곳의 환경은 적대적이므로 훈련을 통해 전투 인원을 배치 가능합니다.")
        messagebox.showinfo("군사창 튜토리얼", "시민의 수가 곧 전투력이지만, 비전투 인원이 제외되기 때문에 군사 훈련은 필수적입니다.")
        messagebox.showinfo("군사창 튜토리얼", "보병들은 공수 양측에서 모두 활약이 가능한 기초적 병종입니다. 안전하게 전투를 진행하기 위해 꼭 필요합니다.")
        messagebox.showinfo("군사창 튜토리얼", "포병들은 박격포나 대포 등의 강력한 화기를 다루며, 공격에서는 안전하면서도 강력한 성능을 보유합니다.")
        messagebox.showinfo("군사창 튜토리얼", "기병들은 무장된 소형 전투기를 탑승하고, 기동성을 살려 선제 공격이 가능합니다.")
        messagebox.showinfo("군사창 튜토리얼", "방어 시설이 부족하다면, 일부의 보병을 통한 추가적인 방어선을 구축하는 것이 좋습니다.")
        messagebox.showinfo("군사창 튜토리얼", "충분한 방어 건물이 지어진 이후에는 기병의 선제 타격을 통해 약한 적들을 쓰러뜨리는 것이 유리합니다.")
        messagebox.showinfo("군사창 튜토리얼", "높은 체력을 바탕으로 전열에서 버티는 적은 포병의 타격으로 빠르게 제거해야 합니다.")
        messagebox.showinfo("군사창 튜토리얼", "이상 설명을 마치겠습니다. 다시 설명을 들으시려면 하단의 도움말 버튼을 클릭하세요.")
    
def ArmyWindow():
    global people
    main.destroy()
    army=Tk()
    army.overrideredirect(True)
    army.geometry("{0}x{1}+0+0".format(army.winfo_screenwidth(), army.winfo_screenheight()))
    functions=Frame(army, height=100)
    functions.pack(side=BOTTOM, fill=X)
    back=Button(functions, text="닫기", font=("맑은 고딕", 20), bg="red", command=army.destroy)
    back.pack(side=RIGHT, padx=50, pady=10)
    helpbtn=Button(functions, text="도움말", font=("맑은 고딕", 20), command=lambda: ArmTut())
    helpbtn.pack(side= RIGHT, padx=50, pady=10)
    frame=Frame(army, height=50, bg="white")
    frame.pack(side=TOP, fill=X)
    Walkers=Label(army, borderwidth=2, relief=SOLID, bg="white")
    Artillery=Label(army, borderwidth=2, relief=SOLID, bg="white")
    Cavalry=Label(army, borderwidth=2, relief=SOLID, bg="white")
    Walkers.pack(fill=X)
    Artillery.pack(fill=X)
    Cavalry.pack(fill=X)

    def Done(bt):
        bt.config(state=DISABLED, bg="blue")
    def Disable(btn):
        btn.config(state=DISABLED)
        
    def TrainTroop(troop):
        global walker
        global mortar
        global crow
        global people
        global apamount
        global darkmatter
        trainnum=askinteger("훈련 인원수 결정", "훈련할 병력 수를 입력하세요. (현재 잔여 인원수 : %d)"%people)
        
        if troop==1:
            if people<trainnum:
                messagebox.showinfo("자원 부족", "인구수가 부족합니다.")
            else:
                people-=trainnum
                walker+=trainnum
                      
        elif troop==2:
            if people<trainnum*3:
                messagebox.showinfo("자원 부족", "인구수가 부족합니다.")
            else:
                people-=trainnum*3
                mortar+=trainnum
               
        elif troop==3:
            if people<trainnum*2:
                messagebox.showinfo("자원 부족", "인구수가 부족합니다.")
            else:
                people-=trainnum*2
                crow+=trainnum
                
    def Update(i):
        if i==0:
            btn00.config(text="보병(%d)"%(walker))
        if i==1:
            btn01.config(text="박격포(%d)"%(mortar))
        if i==2:
            btn02.config(text="까마귀(%d)"%(crow))
    ##병종
    global darkmatterok
    global laserbeamok
    global megaengineok
    btn00=Button(Walkers, text="보병(%d)"%(walker), font=("맑은 고딕", 15),  command=lambda: DoubleFunc(TrainTroop(1), Update(0)))
    btn00.pack(side=LEFT, padx=20, pady=5)
    if people<=0 or laserbeamok==0:
        Disable(btn00)
    btn00.bind("<Button-3>", lambda k : messagebox.showinfo("보병", "공격과 방어의 기본입니다. 전투력 5, 방어력 1, 인력 소모 1"))
    btn01=Button(Artillery, text="박격포(%d)"%(mortar), font=("맑은 고딕", 15),  command=lambda: DoubleFunc(TrainTroop(2), Update(1)))
    btn01.pack(side=LEFT, padx=20, pady=5)
    if people<=0 or darkmatterok==0:
        Disable(btn01)
    btn01.bind("<Button-3>", lambda k : messagebox.showinfo("박격포", "강력한 위력의 한 방을 선사합니다. 전투력 16, 인력 소모 3"))
    btn02=Button(Cavalry, text="까마귀(%d)"%(crow), font=("맑은 고딕", 15),  command=lambda: DoubleFunc(TrainTroop(3), Update(2)))
    btn02.pack(side=LEFT, padx=20, pady=5)
    if people<=0 or megaengineok==0:
        Disable(btn02)
    btn02.bind("<Button-3>", lambda k : messagebox.showinfo("까마귀", "기동력을 활용한 전투가 주 목적인 기병입니다. 전투력 6, 기동력 3, 인력 소모 2"))
    global armtut
    if armtut==1:
        armtut=0
        ArmTut()
        
    army.mainloop()
##영웅창------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def HeroWindow():
    hero=Toplevel()
    heroinfo=Label(hero, text="영웅 정보", font=("맑은 고딕", 15), bg="white")
    heroinfo.pack(side=TOP, fill=X)
    stat=Frame(hero, width=350, bg="green")
    stat.pack(side=RIGHT, fill=X)
    strength=Label(stat, bg="red", fg="yellow", text="힘 : %d"%Str, font=("맑은 고딕", 15))
    dexerity=Label(stat, bg="yellow", fg="blue", text="민첩 : %d"%Dex, font=("맑은 고딕", 15))
    intelligence=Label(stat, bg="magenta", fg="white", text="지능 : %d"%Int, font=("맑은 고딕", 15))
    strength.pack(padx=5, pady=5, side=LEFT)
    dexerity.pack(padx=5, pady=5, side=LEFT)
    intelligence.pack(padx=5, pady=5, side=LEFT)    
##------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def CombatTrophy(a):
    global goldamount
    global goldupdown
    global tpupdown
    global lpupdown
    global wor
    global core, corefrag
    if a==1:
        trophy=Tk()
        trophy.title("전투 보상")
        label=Label(trophy, text="외계인들이 지니고 있던 장신구들을 획득했습니다.(골드 +100)", font=("맑은 고딕", 10))
        label.pack(fill=BOTH)
        goldamount+=100
    if a==2:
        trophy=Tk()
        trophy.title("전투 보상")
        label=Label(trophy, text="야수 소굴에서 금맥을 발견했습니다.(턴당 골드+10)", font=("맑은 고딕", 10))
        label.pack(fill=BOTH)
        goldupdown+=10
    if a==3:
        trophy=Tk()
        trophy.title("전투 보상")
        label=Label(trophy, text="골렘의 파편에서 신비한 동력원을 발견했습니다.(턴당 연구력 +5)", font=("맑은 고딕", 10))
        label.pack(fill=BOTH)
        corefrag+=1
    if a==4:
        trophy=Tk()
        trophy.title("전투 보상")
        label=Label(trophy, text="외계인 포로들을 노예로 삼았습니다.(노동자 +5)", font=("맑은 고딕", 10))
        label.pack(fill=BOTH)
        wor+=5
    if a==5:
        trophy=Tk()
        trophy.title("전투 보상")
        label=Label(trophy, text="야수의 무덤을 발견했습니다.(골드 +250)", font=("맑은 고딕", 10))
        label.pack(fill=BOTH)
        goldamount+=250
    if a==6:
        trophy=Tk()
        trophy.title("전투 보상")
        label=Label(trophy, text="골렘의 동력원을 온전히 챙겨냈습니다.(턴당 노동력+15)", font=("맑은 고딕", 10))
        label.pack(fill=BOTH)
        core+=1
##전투 시스템----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
def AtkEnemy(i):
    global ailencurhp, ailen, ailenskill, ailenatk, apamount
    global beastcurhp, beast, beastskill, beastatk
    global golemcurhp, golem, golematk
    global shamancurhp, shaman, shamanatk
    global walker, walkerpower, mortar, mortarpower, crow, crowpower, people, fortressok

    
    def Atk(curhp, enemy, atk):
        global apamount, Str, fortressok, ailencurhp, golemcurhp, beastcurhp
        global walker, crow, mortar, people, mortarpower, walkerpower, crowpower, ailen, golem, beast
        curhp=curhp-apamount-Str
        
        messagebox.showinfo("공격!", "적을 공격하여 %d의 피해를 입혔습니다."%(apamount+Str))
        if curhp<=0:
            curhp=0
            messagebox.showinfo("승리!", "적을 물리쳤습니다!")
            if enemy==1:
                ailen, ailencurhp=0, 0
            elif enemy==2:
                golem, golemcurhp=0, 0
            elif enemy==3:
                beast, beastcurhp=0, 0
            combat.destroy()
            
        else:
            damage=atk
            dmg=damage
            walkernum=walker
            walker-=damage/5
            if walker<0:
                walker=0
                damage-=walkernum*5
            else:
                damage-=(walkernum-walker)*5
            if damage>0:
                crownum=crow
                crow-=damage/9
                if crow<0:
                    crow=0
                    damage-=crownum*9
                else:
                    damage-=(crownum-crow)*9
            if damage>0:
                mortarnum=mortar
                mortar-=damage/12
                if mortar<0:
                    mortar=0
                    damage-=mortarnum*12
                else:
                    damage-=(mortarnum-mortar)*12
            if damage>0:
                people-=damage
                    
            messagebox.showinfo("공격받음!", "남은 전력 : 시민군 %d명, 보병 %d명, 박격포 %d기, 까마귀 %d기"%(people, walker, mortar, crow))
            combat.destroy()
            apamount=people+mortar*mortarpower+walker*walkerpower+crow*crowpower+fortressok*50
            if enemy==1:
                ailencurhp=curhp
            elif enemy==3:
                beastcurhp=curhp
            elif enemy==2:
                golemcurhp=curhp
            if apamount<=0:
                GameOver()

    if i==1:
        Atk(ailencurhp, 1, ailenatk)
    if i==2:
        Atk(beastcurhp, 3, beastatk)
    if i==3:
        Atk(golemcurhp, 2, golematk)
    if i==4:
        shamancurhp=shamancurhp-apamount-Str
        messagebox.showinfo("공격!", "적을 공격하여 %d의 피해를 입혔습니다."%(apamount+Str))
        if shamancurhp<=0:
            shamancurhp=0
            messagebox.showinfo("승리!", "적을 물리쳤습니다!")
            shaman=0
            combat.destroy()
            gameover=Tk()
            gameover.geometry('1000x600')
            label=Label(gameover, text="당신은 1달 동안 개척지를 무사히 지켜냈습니다. 앞으로 이 행성에서 인류가 번성해 나갈 수 있을까요?\n당신의 점수: %d"%(goldamount), font=("맑은 고딕", 15))
            label.pack(fill=BOTH)
            btn=Button(gameover, text="종료", font=("맑은 고딕", 15), command=quit)
            btn.pack()
            
        else:
            damage=shamanatk
            dmg=damage
            walkernum=walker
            walker-=damage/5
            if walker<0:
                walker=0
                damage-=walkernum*5
            else:
                damage-=(walkernum-walker)*5
            if damage>0:
                crownum=crow
                crow-=damage/9
                if crow<0:
                    crow=0
                    damage-=crownum*9
                else:
                    damage-=(crownum-crow)*9
            if damage>0:
                mortarnum=mortar
                mortar-=damage/12
                if mortar<0:
                    mortar=0
                    damage-=mortarnum*12
                else:
                    damage-=(mortarnum-mortar)*12
            if damage>0:
                people-=damage
                
            messagebox.showinfo("공격받음!", "남은 전력 : 시민군 %d명, 보병 %d명, 박격포 %d기, 까마귀 %d기"%(people, walker, mortar, crow))
            combat.destroy()
            apamount=people+mortar*mortarpower+walker*walkerpower+crow*crowpower+50*fortressok
            if apamount<=0:
                GameOver()
          
def Def(atk):
    global walker, crow, mortar, people, walkerpower, mortarpower, crowpower, fortressok, apamount, defence
    if defence>=atk:
                messagebox.showinfo(" ", "막기 성공!")
                combat.destroy()
    else:
        damage=atk-defence
        dmg=damage
        walkernum=walker
        walker-=damage/5
        if walker<0:
            walker=0
            damage-=walkernum*5
        else:
            damage-=(walkernum-walker)*5
        if damage>0:
            crownum=crow
            crow-=damage/9
            if crow<0:
                crow=0
                damage-=crownum*9
            else:
                damage-=(crownum-crow)*9
        if damage>0:
            mortarnum=mortar
            mortar-=damage/12
            if mortar<0:
                mortar=0
                damage-=mortarnum*12
            else:
                damage-=(mortarnum-mortar)*12
        if damage>0:
            people-=damage
        messagebox.showinfo("공격받음!", "남은 전력 : 시민군 %d명, 보병 %d명, 박격포 %d기, 까마귀 %d기"%(people, walker, mortar, crow))
        combat.destroy()
        apamount=people+mortar*mortarpower+walker*walkerpower+crow*crowpower+50*fortressok
        if apamount<=0:
            GameOver()
    
def DefEnemy(i):
    global Dex, walkerdef, walker, ailenatk, beastatk, golematk, shamanatk, defence
    defence=random.randrange(1, Dex)+walkerdef*walker
    if i==1:
        Def(ailenatk)
    if i==2:
        Def(beastatk)
    if i==3:
        Def(golematk)
    if i==4:
        Def(shamanatk)
            
def FleeEnemy(i):
    global fleeok, ailen, beast, golem
    fleeok=random.randrange(1, 6)
    if i==1:
        if fleeok==1:
            messagebox.showinfo("", "도망 성공!!!")
            ailen=0
            combat.destroy()
        else:
            DefEnemy(1)
    if i==2:
        if fleeok==1:
            messagebox.showinfo("", "도망 성공!!!")
            beast=0
            combat.destroy()
        else:
            DefEnemy(2)
    if i==3:
        if fleeok==1:
            messagebox.showinfo("", "도망 성공!!!")
            golem=0
            combat.destroy()
        else:
            DefEnemy(3)    
##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##메인 함수의 시작------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    ##메인 창이 실행되기 전에 실행될 것들
    ##타이틀 실행
    if start==1:
        start=0
        TitleScreen()
            
    ##30일까지 진행시
    if day==30:
        while True:
            if fscount==1:
                shamancurhp-=crow*crowspeed
                fscount-=fs
                if shamancurhp<=0 and shaman==1:
                    shamancurhp=0
                    shaman=0
                    win=Tk()
                    win.title("전투 정보")
                    label=Label(win, text="기병대의 선제 타격으로 적 샤먼을 처치했습니다.", font=("맑은 고딕", 10))
                    fscount=1
                    label.pack(fill=BOTH)
                    if shamancurhp<=0:
                        shamancurhp=0
                        messagebox.showinfo("승리!", "적을 물리쳤습니다!")
                        shaman=0
                        combat.destroy()
                        gameover=Tk()
                        gameover.geometry('1000x600')
                        label=Label(gameover, text="당신은 1달 동안 개척지를 무사히 지켜냈습니다. 앞으로 이 행성에서 인류가 번성해 나갈 수 있을까요?\n당신의 점수: %d"%(goldamount), font=("맑은 고딕", 15))
                        label.pack(fill=BOTH)
                        btn=Button(gameover, text="종료", font=("맑은 고딕", 15), command=quit)
                        btn.pack()
                    break
            
            if shaman==1:
                
                skill=random.randrange(1, 5)
                combat=Tk()
                combat.title("주술사의 군대와 전투!")
                combat.geometry('600x250+200+100')
                combat.resizable(0, 0)
                portrait=Canvas(width=64, height=64, bg="white")
                portrait.pack(anchor=NW, padx=5, pady=5)
                moninfo=Frame(width=128, height=64, bg="white")
                moninfo.pack(anchor=NW, padx=5, pady=5)
                monhp=Label(moninfo, text="HP : %d /%d"%(shamancurhp, shamanmaxhp), bg="red")
                monhp.pack(side=TOP)
                combatmenu=Frame(combat, height=50, bg="green")
                combatmenu.pack(side=BOTTOM, fill=X)
                attack=Button(combatmenu, text="공격", command=lambda: AtkEnemy(4))
                defense=Button(combatmenu, text="방어", command=lambda: DefEnemy(4))
                attack.pack(side=LEFT, padx=5, pady=5)
                defense.pack(side=LEFT, padx=5, pady=5)
                if bosscount==1:
                    messagebox.showinfo("...", "저 멀리서 외계의 군대가 다가옵니다.")
                    messagebox.showinfo("주술사", "모두 공격!")
                    bosscount=0
                if skill==1:
                    messagebox.showinfo("정보", "주술사가 치유의 주문을 암송합니다.")
                    shamancurhp+=500
                    shamanatk=0
                if skill==2:
                    messagebox.showinfo("정보", "주술사가 강화의 주문을 암송합니다.")
                    shamanatk+=100
                    apamount=people+mortar*mortarpower+walker*walkerpower+crow*crowpower+100+50*fortressok
                if skill==3:
                    messagebox.showinfo("정보", "주술사가 광기의 주문을 퍼뜨립니다. 아군 또한 주문에 걸렸습니다.")
                    shamanatk+=150
                if skill==4:
                    messagebox.showinfo("정보", "주술사의 주문이 실패했습니다!")
                    shamanatk=0
                
                combat.mainloop()
                apamount=people+mortar*mortarpower+walker*walkerpower+crow*crowpower+50*fortressok
                shamanatk=150
                    
        ##보스 클리어
        
    ##외계인과의 전투
    while True:
        if fscount==1:
            if ailen==1:
                ailencurhp-=crow*crowspeed
                fscount-=fs
            if ailencurhp<=0 and ailen==1:
                ailencurhp=0
                ailen=0
                win=Tk()
                win.title("전투 정보")
                label=Label(win, text="기병대의 선제 타격으로 외계인 정찰대를 처치했습니다. 기병대는 내일 전리품을 챙겨 돌아옵니다.", font=("맑은 고딕", 10))
                fscount=1
                label.pack(fill=BOTH)
                break
            
        if ailen==1:
            
            combat=Tk()
            combat.title("외계인 정찰대와 전투!")
            combat.geometry('600x250+200+100')
            combat.resizable(0, 0)
            portrait=Canvas(width=64, height=64, bg="white")
            portrait.pack(anchor=NW, padx=5, pady=5)
            moninfo=Frame(width=128, height=64, bg="white")
            moninfo.pack(anchor=NW, padx=5, pady=5)
            monhp=Label(moninfo, text="HP : %d /%d"%(ailencurhp, ailenmaxhp), bg="red")
            monhp.pack(side=TOP)
            combatmenu=Frame(combat, height=50, bg="green")
            combatmenu.pack(side=BOTTOM, fill=X)
            attack=Button(combatmenu, text="공격", command=lambda: AtkEnemy(1))
            defense=Button(combatmenu, text="방어", command=lambda: DefEnemy(1))
            flee=Button(combatmenu, text="도망", command=lambda: FleeEnemy(1))
            if ailenskill!=0:
                attack.pack(side=LEFT, padx=5, pady=5)
            defense.pack(side=LEFT, padx=5, pady=5)
            if ailenskill!=0:
                flee.pack(side=LEFT, padx=5, pady=5)
            if ailenskill==0:
                ailenskill=3
                messagebox.showinfo("정보", "외계인 정찰대가 마비를 사용합니다!")
                messagebox.showinfo("정보", "마비에 걸려 일시적으로 방어만 가능합니다.")
            combat.mainloop()
            if ailen==1:
                ailenskill-=1
        elif ailen==0:
            ailenskill=3
            if ailencurhp==0:
                ailenloot=random.randrange(0, 10)
                ailencurhp=ailenmaxhp
                if ailenloot==9:
                    CombatTrophy(4)
                else:
                    CombatTrophy(1)
            fscount=1
            break

    while True:
        
        if fscount==1:
            if beast==1:
                beastcurhp-=crow*crowspeed
                fscount-=fs
            if beastcurhp<=0 and beast==1:
                beastcurhp=0
                beast=0
                win=Tk()
                win.title("전투 정보")
                label=Label(win, text="기병대의 선제 타격으로 야수 무리를 처치했습니다. 기병대는 내일 전리품을 챙겨 돌아옵니다.", font=("맑은 고딕", 10))
                fscount=1
                label.pack(fill=BOTH)
                break
            
        if beast==1:
            if beastskill==0:
                beastcurhp+=300
                beastatk+=70
                beastmaxhp+=300
            combat=Tk()
            combat.title("야수 떼와 전투!")
            combat.geometry('600x250+200+100')
            combat.resizable(0, 0)
            portrait=Canvas(width=64, height=64, bg="white")
            portrait.pack(anchor=NW, padx=5, pady=5)
            moninfo=Frame(width=128, height=64, bg="white")
            moninfo.pack(anchor=NW, padx=5, pady=5)
            monhp=Label(moninfo, text="HP : %d /%d"%(beastcurhp, beastmaxhp), bg="red")
            monhp.pack(side=TOP)
            combatmenu=Frame(combat, height=50, bg="green")
            combatmenu.pack(side=BOTTOM, fill=X)
            attack=Button(combatmenu, text="공격", command=lambda: AtkEnemy(2))
            defense=Button(combatmenu, text="방어", command=lambda: DefEnemy(2))
            flee=Button(combatmenu, text="도망", command=lambda: FleeEnemy(2))
            attack.pack(side=LEFT, padx=5, pady=5)
            defense.pack(side=LEFT, padx=5, pady=5)
            flee.pack(side=LEFT, padx=5, pady=5)
            if beastskill==0:
                beastskill=2
                messagebox.showinfo("정보", "야수들이 무리를 불러냅니다! 야수들의 수가 늘어나 더 강해졌습니다.")
            combat.mainloop()
            if beast==1:
                beastskill-=1
        elif beast==0:
            beastskill=2
            if beastcurhp==0:
                beastloot=random.randrange(0, 5)
                beastcurhp=beastmaxhp
                if beastloot==4:
                    CombatTrophy(5)
                else:
                    CombatTrophy(2)
            fscount=1
            break

    while True:
        if fscount==1:
            if golem==1:
                golemcurhp-=crow*crowspeed
                fscount-=fs
            if golemcurhp<=0 and golem==1:
                golemcurhp=0
                golem=0
                win=Tk()
                win.title("전투 정보")
                label=Label(win, text="기병대의 선제 타격으로 적 골렘을 처치했습니다. 기병대는 내일 전리품을 챙겨 돌아옵니다.", font=("맑은 고딕", 10))
                fscount=1
                label.pack(fill=BOTH)
                break
   
        if golem==1:
            combat=Tk()
            combat.title("거대 골렘과 전투!")
            combat.geometry('600x250+200+100')
            combat.resizable(0, 0)
            portrait=Canvas(combat, width=64, height=64, bg="white")
            portrait.pack(anchor=NW, padx=5, pady=5)
            moninfo=Frame(combat, width=128, height=64, bg="white")
            moninfo.pack(anchor=NW, padx=5, pady=5)
            monhp=Label(moninfo, text="HP : %d /%d"%(golemcurhp, golemmaxhp), bg="red")
            monhp.pack(side=TOP)
            combatmenu=Frame(combat, height=50, bg="green")
            combatmenu.pack(side=BOTTOM, fill=X)
            attack=Button(combatmenu, text="공격", command=lambda: AtkEnemy(3))
            defense=Button(combatmenu, text="방어", command=lambda: DefEnemy(3))
            flee=Button(combatmenu, text="도망", command=lambda: FleeEnemy(3))
            attack.pack(side=LEFT, padx=5, pady=5)
            skill=random.randrange(0, 2)
            if skill!=0:
                defense.pack(side=LEFT, padx=5, pady=5)
            if skill!=1:
                flee.pack(side=LEFT, padx=5, pady=5)

            if skill==0:
                info1=Toplevel()
                info1.title("정보")
                label=Label(info1, text="골렘이 땅을 울려 전열을 가다듬지 못합니다!")
            if skill==1:
                info2=Toplevel()
                info2.title("정보")
                label=Label(info2, text="골렘이 돌을 던져 퇴로를 차단합니다!")
            combat.mainloop()
        elif golem==0:
            if golemcurhp==0:
                golemloot=random.randrange(0, 15)
                if golemloot==14:
                    CombatTrophy(6)
                else:
                    CombatTrophy(3)
                golemcurhp=golemmaxhp
            fscount=1
            break
##메인 창 실행------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if buildskillok==1:
        labortier=2
    apamount=people+mortar*mortarpower+walker*walkerpower+crow*crowpower+fortressok*50
    walkerdef=1+(walker*bunkernum)/10
    goldupdown=recyclenum*10
    lpupdown=wor*worpow+corefrag*5
    tpupdown=sch*schpow+Int+core*15
    main=Tk()
    main.title('테라포밍')
    main.overrideredirect(True)
    main.geometry("{0}x{1}+0+0".format(main.winfo_screenwidth(), main.winfo_screenheight()))
    
    ##자원 표시줄
    resources=Frame(main, height=60, bg="yellow")
    resources.pack(fill=X, side=TOP)
    resourcesinfo=Label(resources, text="금=%d(+%d)     노동력=%d(+%d)     군사력=%d     기술력=%d(+%d)     인구수=%d     %d일차"%(goldamount, goldupdown, lpamount, lpupdown, apamount, tpamount, tpupdown, people, day), bg="yellow")
    resourcesinfo.config(font=("맑은 고딕", 20))
    resourcesinfo.pack(anchor=W)
    
    ##우측 버튼들
    buttons=Frame(main,width=150, bg="green")
    buttons.pack(side=RIGHT, fill=Y)
    herostatus=Button(buttons, text="영웅 상태창", command=HeroWindow)
    herostatus.config(font=("맑은 고딕", 30))
    herostatus.pack(side=TOP, pady=5)
    army=Button(buttons, text="병력", command=ArmyWindow)
    army.config(font=("맑은 고딕", 30))
    army.pack(side=TOP, pady=5)
    techb=Button(buttons, text="기술", command=TechWindow)
    techb.config(font=("맑은 고딕", 30))
    techb.pack(side=TOP, pady=5)
    labor=Button(buttons, text="작업", command=LaborWindow)
    labor.config(font=("맑은 고딕", 30))
    labor.pack(side=TOP, pady=5)
    dayplus=Button(buttons, text="하루를 마친다", command=NextDay)
    dayplus.config(font=("맑은 고딕", 30))
    dayplus.pack(side=TOP, pady=5, padx=5)
    
    ##지도
    Map=Frame(main, width=main.winfo_screenwidth(), height=700, bg="white")
    Map.pack(side=LEFT, fill=BOTH)
    
    ##메뉴
    menu=Menu(main)
    main.config(menu=menu)
    menu.config(font=("맑은 고딕", 30))
    submenu=Menu(menu)
    menu.add_cascade(label="메뉴", menu=submenu)
    submenu.config(font=("맑은 고딕", 15))
    submenu.add_command(label="종료", command=quit)
    submenu.add_command(label="튜토리얼", command=Tutorial)

    ##튜토리얼
    
    
    if daycountinfo==1:
        daycountinfo=0
        messagebox.showinfo("알림", "%d번째 날이 밝았습니다!"%day)
    if tut==1:
        tut=0
        Tutorial()
   
    
    main.mainloop()
