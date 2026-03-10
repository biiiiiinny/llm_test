import google.generativeai as genai
import os

# 1. API 키 설정 (본인의 API 키로 교체)
genai.configure(api_key="")

# 2. 모델 설정
model = genai.GenerativeModel('gemini-2.5-flash-lite')

def analyze_presentation(script):
    # 3. 프롬프트 시나리오 작성
    prompt = f"""
    당신은 발표 전문가입니다. 다음 제공된 [발표 스크립트]를 분석하여 피드백을 주세요.
    
    [발표 스크립트]:
    {script}
    
    [요청 사항]:
    1. 전체 구조를 [서론]-[본론]-[결론]으로 명확히 구분하여 요약하세요.
    2. 각 섹션별 핵심 내용을 한 줄로 정리하세요.
    3. 발표의 논리적 흐름과 전달력 향상을 위한 개선 피드백을 3가지 제안하세요.
    
    [출력 형식]:
    - 서론: (내용)
    - 본론: (내용)
    - 결론: (내용)
    - 피드백: 1, 2, 3
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"에러가 발생했습니다: {str(e)}"

# 4. 실행 테스트
full_script = """
안녕하세요, 오늘 저는 인공지능의 미래에 대해 발표할 '홍길동'입니다. 
먼저 인공지능 기술의 현재 위치를 살펴보겠습니다. 
최근 LLM 기술은 비약적으로 발전하여 우리 삶의 많은 부분을 바꾸고 있습니다. 
하지만 데이터 편향성 같은 문제도 여전히 존재하죠. 
따라서 우리는 기술 발전과 윤리적 고민을 병행해야 합니다. 
이상으로 발표를 마치겠습니다. 들어주셔서 감사합니다.
"""

result = analyze_presentation(full_script)
print(result)