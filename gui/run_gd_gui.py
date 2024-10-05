import gradio as gr

# gradio 내부에서 사용할 함수
def greet(name):
    return f"Hello, {name}!"

# block 단위로 인터페이스 구성
# with문을 사용하여 gr.Blocks() 내에서 정의한 요소들이
# iface라는 인터페이스로 연결
with gr.Blocks() as iface:
    # gr.Markdown() : 마크다운 형식의 텍스트를 웹페이지에 표시
    # "Hello world!"가 마크다운 형식으로 화면에 나타남
    gr.Markdown("Hello, world!")
    # gr.Row()는 그리드 형태로 여러 컴포넌트를 한 줄에 배치할 수 있도록 하는 컨테이너
    with gr.Row():
        # inp = 입력 받을 텍스트 박스
        # placeholder = 사용자가 아무것도 입력하지 않았을 때 보이는 안내 텍스트
        inp = gr.Textbox(placeholder = "What's your name?")
        # out = 결과를 출력할 텍스트 박스
        out = gr.Textbox()
    # btn은 "submit"이라는 텍스트가 있는 버튼을 생성 -> 클릭 시 이벤트가 발생
    btn = gr.Button("Submit")
    # btn.click() = 버튼이 클릭될 때 어떤 동작을 할 지 정의하는 메소드
    # fn = update : 버튼 클릭 시 update 함수 호출
    # inputs = inp : inp 텍스트박스 입력값을 update 함수에 전달
    # outputs = out : update 함수의 결과값을 out 텍스트 박스에 출력
    btn.click(fn = greet, inputs = inp, outputs = out)

# 챗봇에 채팅이 입력되면 이 함수를 호출
# message : 유저의 채팅 메시지, history는 채팅 기록
# additional_input_info : additional_inputs 안 블록의 정보를 받음
def response(message, history, additional_input_info):
    # additional_input_info의 텍스트를 챗봇 대답 뒤에 추가
    return "Chatbot is not completed yet" + additional_input_info

gr.ChatInterface(
    fn = response,
    textbox = gr.Textbox(placeholder = "Tell me something", container = False, scale = 7),
    title = "What kind of chatbots do you want?",
    description = "chatbot that answer to what you ask",
    theme = "soft",
    examples = [["Hi"], ["It's so cold"], ["Recommend lunch menu"]],
    retry_btn = "Resend",
    undo_btn = "Delete Previous chat",
    clear_btn = "Delete Entire chat",
    additional_inputs = [gr.Textbox("!!!", label = "Word chain")]
).launch()

# Gradio 인터페이스 실행하는 메소드
# 호출하면 로컬 서버가 실행되고 웹브라우저에서 해당 페이지 볼 수 있음
# share = True를 통해 공개 링크 생성
iface.launch(share = True)
