import streamlit as st
import pandas as pd
import joblib
from joblib import dump, load
from PIL import Image
import streamlit.components.v1 as components
from streamlit.components.v1 import iframe

HairG = Image.open("hairgrowP.jpg")
Skindarken = Image.open("skin darkenP.jpg")


st.write(""" ## แอปประเมินความเสี่ยงโรคถุงน้ำรังไข่หลายใบ

ว่าคุณจะมีความเสี่ยงเป็นโรคถุงน้ำในรังไข่หลายใบหรือไม่

<<< หากไม่พบแบบประเมิน คลิกลูกศรมุมซ้ายบนเพื่อเปิดทำการประเมินความเสี่ยง

""")
left, right, = st.columns(2)

left.write('แบบประเมินความเสี่ยงโรคถุงน้ำรังไข่หลายใบ')
left.write('กรอกข้อมูล')
form = left.form("template_form")



# รับ User input feature  X 
def user_input_features():
  Age = form.slider('อายุเท่าไหร่',0,100,22)
  Weight= form.slider('น้ำหนัก (Kg)เท่าไหร่',0,150,79)
  Cycle = form.slider('ประจำเดือนมากี่วัน',0,31,7)
  Cycle = form.slider('ประจำเดือนมากี่วัน',0,31,7)
  CycleLength= form.slider('ระยะห่างของรอบเดือน ห่างกันกี่วัน',0,60,16)
  HairGrowth = form.slider('ขนตามจุดต่างๆเพิ่มขึ้นหรือไม่ ',0,1,1)
  SkinDarkening= form.slider('ผิวดำคล้ำตามข้อต่างๆหรือไม่',0,1,0)
  Pimples= form.slider('สิวเพิ่มขึ้นหรือไม่',0,1,1)
  Fastfood= form.slider('รับประทานอาหารที่มีไขมันสูง (Fastfood) ',0,1,0)
  FollicleL= form.slider('หน้ามันรูขุมขนทางด้านซ้าย กว้างขึ้นหรือไม่',0,1,1)
  FollicleR= form.slider('หน้ามันรูขุมขนทางด้านขวา กว้างขึ้นหรือไม่',0,1,1)
  WeightGain= form.slider( 'ช่วงนี้น้ำหนักเพิ่มขึ้นหรือไม่',0,1,1)
  
  
  left.write('อายุ', Age,'ปี')
  left.write(' # --------------------------------------')
  
  
  left.write('น้ำหนัก', Weight, 'กิโลกรัม')
  left.write(' # --------------------------------------')
  
  
  left.write('รอบเดือนมา', Cycle, 'วัน')
  left.write(' # --------------------------------------')
  
  
  left.write('ระยะห่างของรอบเดือน', CycleLength, 'วัน')
  left.write(' # --------------------------------------')
  left.write('### สอบถามอาการ ใช่(1)หรือไม่(0) ')
  
  left.caption('''สังเกตตามจุดต่างๆบนร่างกาย ว่ามีขนเพิ่มขึ้นหรือไม่ เช่น จากไม่มีขนเลย เพิ่มขึ้นไประดับ1 หรือ มีขนที่ระดับ3แล้วเพิ่มขึ้นไประดับ4 ''')
  left.write('ขนเพิ่มขึ้นหรือไม่', hairGrowth)
  left.image(HairG, use_column_width = True)
  left.write(' # --------------------------------------')
 
  
  left.caption('ผิวคล้ำดำหนา ตามจุด ข้อนิ้ว ข้อศอก คอ หรือ รักแร้ เป็นต้น')
  left.image(Skindarken, use_column_width = True)
  left.write('ผิวดำคล้ำตามข้อต่างๆ', SkinDarkening)
  left.write(' # --------------------------------------')
  

  
  left.caption('สังเกตตนเองหากปกติไม่มีสิว แล้วสิวเกิดขึ้นมาเกินไป หากมีสิวขึ้นเยอะอยู่แล้วไม่ได้เพิ่มขึ้นถือว่าปกติ')
  left.write('สิวเกิดเพิ่มขึ้น', Pimples)
  left.write(' # --------------------------------------')
  

  
  left.write('ทานอาหารที่มีไขมันสูงหรือไม่', Fastfood)
  left.caption('ชอบรับประทานอาหารที่มีไขมันสูง หรือ ทานบ่อยครั้ง')
  left.write(' # --------------------------------------')
  

  
  left.write('หน้ามันและรูขุมขนกว้างทางด้านซ้ายหรือไม่', FollicleL)
  left.write(' # --------------------------------------')
  

  
  left.write('หน้ามันและรูขุมขนกว้างทางด้านขวาหรือไม่' , FollicleR)
  left.write(' # --------------------------------------')
  

  
  left.caption('น้ำหนักเพิ่มขึ้นแบบรวดเร็วหรือไม่ เช่น จาก60เพิ่มไป 70 ในระยะเวลาสั้นๆ')
  left.write('น้ำหนักเพิ่มขึ้น', WeightGain)
  left.write(' # --------------------------------------')
  
  pipe =  { 'Age (yrs)': Age,
           'Weight (Kg)': Weight,
           'Cycle(R/I)': Cycle,
           'Cycle length(days)': CycleLength,
           'hair growth(Y/N)': HairGrowth,
           'Skin darkening (Y/N)': SkinDarkening,
           'Pimples(Y/N)': Pimples,
           'Fast food (Y/N)': Fastfood,
           'Follicle No. (L)': FollicleL,
           'Follicle No. (R)': FollicleR,
           'Weight gain(Y/N)': WeightGain}
  features = pd.DataFrame(pipe, index=[0])
  return features
submit = form.form_submit_button("ประเมินความเสี่ยง")

app  = load('PcosApp.joblib')

name = ['''negative

ท่านมีความเสี่ยงน้อย




''', '''possitive

ท่านมีความเสี่ยง 


สามรถดูแลสุขภาพตนเอง  โดยการออกกำลังกาย และรับทานอาหารครบ 5 หมู่
*ควร เลี่ยงทานอาหารที่มีไขมันสูง*  และพบแพทย์ผู้เชี่ยวชาญสำหรับการวินิจฉัยโรคต่อไป 
ศึกษาเกี่ยวกับโรคเพิ่มเติม  
https://www.bangkokhospital.com/content/overweight-women-are-more-likely-to-face-polycystic-ovary-syndrome


''']

df = user_input_features()

right.subheader('ทำการประเมินความเสี่ยง')
right.write(df)

prediction = app.predict(df)
prediction_proba = app.predict_proba(df)

st.balloons()


st.subheader('ผลการทำนาย (Prediction)')
#st.write([prediction])
right.success(name[prediction[0]])

right.subheader('เปอร์เซ็นความเสี่ยง (Prediction Probability)')
right.write('โอกาสเสี่ยงน้อย','|',  'โอกาสเสี่ยงมาก')
right.write(prediction_proba)


right.write('''รบกวนทำแบบสอบถามประสิทธิภาพของแบบทดสอบ
 ว่ามีการประเมินได้ถูกต้องมากแค่ไหน ''')

# embed streamlit docs in a streamlit app
components.iframe("https://forms.gle/u7GK9hvWkpWjJjaD9")
