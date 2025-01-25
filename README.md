# AIM-Sniper-Project 개요

- 취업 인사이트 및 정보를 판매하는 B2C 마켓 서비스를 개발했습니다.
- `실제 운영`하며 사용자 `118 명`을 확보하였습니다.
- `정량•정성적 설문`을 통해 타겟의 pain point 파악 및 유입 전략을 수립 및 실행하였습니다.
- 오픈 베타 테스트 후, `사용자 로그 분석`, `퍼널 분석`을 통해 유입 현황을 파악하였습니다.
- `기여 내용`
    - 주제 도출, 서비스 이용 데이터 분석, 요약 보고서 생성 시스템 개발, 데이터 ETL 시스템 구축, 웹 UI 디자인
- 참고자료
    - **Website**  ⇒  [AIM | 기업 핵심 정보 분석 및 AI 모의면접](https://aim-sniper.com/companyReport/list)

<br><br>
        
# AIM-Sniper-Project 내용

## ✔️ 데이터 분석
> **1단계: 설문조사**
> 
- 목적: 서비스 초기 아이디어 검증 및 사용자 요구 파악
- 사용 도구 및 방법론:
    - Google Forms 설문조사 설계 (5문항, 3분 이내)
    - Google Forms 내부 툴을 활용하여 데이터 시각화
- 과정:
    - 70명의 응답 데이터 수집
    - 주요 변수: 서비스 이용 목적, 관심 데이터, 유료화 긍정도
    - 가설 설정: “취준생은 기업 정보를 자소서/면접에 활용하는 데 사용할 것이다”
- 결과:
    - 유사 지표를 결합하여 사용자의 Needs 파악 및 전략 수립
    - 분석한 사용자 Needs를 바탕으로 서비스 내 상품 경쟁력 확보  
      <img src="https://github.com/user-attachments/assets/87d85eab-6211-4a99-ac2e-1fd30d82c3b1"
        width=200 />  
      ▲ 1차 서비스 수요 설문조사(09.20) 분석 문서 중 일부 발췌

<br>

> **2단계: 비즈니스 분석**
> 
- 목적: 서비스 가치 창출 및 기획 발표 정리
- 사용 도구 및 방법론:
    - 3C 분석, 시장조사 방법론
    - `Matplotlib`로 시장규모 시각화 (*출처: 통계청)
- 과정:
    - 시장 점유율과 성장 가능성 평가
    - 경쟁사 5곳의 주요 기능과 서비스 차별화 요소 비교
- 결과:
    - ‘사용자 친화적 상품’, ‘운영 비용 절감’을 소구점 설정  
      <img src="https://github.com/user-attachments/assets/558eb96a-150c-4afe-90b4-bc253863f753"
        width=200 />  
      ▲ 'AIM-Sniper' 기획안

<br>

> **3단계: 오픈 베타 서비스 성과 분석**
> 
- 목적: 오픈 이후 사용자 트래픽 및 서비스 성과 측정
- 사용 도구 및 방법론:
    - 주요 KPI: 활성 유저수, 페이지 조회수, 유입 경로
    - `Tableau`로 대시보드 제작
- 과정:
    - :googleanalytics: Google Analytics를 활용한 실시간 사용자 데이터 수집
    - 페이지 조회수, 디바이스 구분, 이탈율 지표를 활용하여 서비스 이용 여정 `퍼널 분석` 진행
- 결과:
    - 서비스 이용 단계에서 모바일 고객의 대규모 이탈
        - 모바일 고객이 일반 서비스 이용 단계로 전환되지 않음(100% 이탈)
        - 해당 단계에서 반응형 웹의 미적용으로 인한 사용성 저하로 보임
          <img src="https://github.com/user-attachments/assets/409946b1-f394-44dc-9fe7-01102ed3d7ac"
               width=500 />  
          ▲ 오픈 베타 서비스 성과 대시보드

<br>

**※ 발표 영상** [AIM-Sniper 서비스 발표 (Data 파트)](https://youtu.be/Zl2SJJ-TyVg?t=3314)
