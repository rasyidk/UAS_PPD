import streamlit as st
import numpy as np
import pickle

st.set_page_config(
    page_title="Chronic Kidney Disease Prediction",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
    <style>
    .main {
        padding: 20px;
    }
    .stButton>button {
        width: 100%;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def load_model():
    with open('model/random_forest_model1.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    st.title('🏥 Chronic Kidney Disease Prediction')
    st.markdown("""
    ### Please fill in the patient's information below
    All fields are required for accurate prediction.
    """)
    
    try:
        model = load_model()
        tab1, tab2, tab3 = st.tabs(["📊 Basic Information", "🔬 Laboratory Results", "📋 Medical History"])

        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                age = st.number_input('Age (years)', min_value=1, max_value=100, value=40, help='Enter age in years')
                bp = st.number_input('Blood Pressure (mm/Hg)', min_value=50, max_value=180, value=80, help='Enter blood pressure in mm/Hg')
            
            with col2:
                appet = st.radio('Appetite', ['good', 'poor'], help='Select appetite condition')
                pe = st.radio('Pedal Edema', ['yes', 'no'], help='Select if pedal edema is present')
                ane = st.radio('Anemia', ['yes', 'no'], help='Select if anemia is present')
        
        with tab2:
            col1, col2 = st.columns(2)
            with col1:
                sg = st.selectbox('Specific Gravity', [1.005, 1.010, 1.015, 1.020, 1.025], 
                                help='Select specific gravity value')
                al = st.selectbox('Albumin', [0, 1, 2, 3, 4, 5], help='Select albumin level')
                su = st.selectbox('Sugar', [0, 1, 2, 3, 4, 5], help='Select sugar level')
                bgr = st.number_input('Blood Glucose Random (mgs/dl)', min_value=0, max_value=500, value=100,
                                    help='Enter blood glucose random in mgs/dl')
                bu = st.number_input('Blood Urea (mgs/dl)', min_value=0, max_value=200, value=40,
                                   help='Enter blood urea in mgs/dl')
                sc = st.number_input('Serum Creatinine (mgs/dl)', min_value=0.0, max_value=15.0, value=1.0,
                                   help='Enter serum creatinine in mgs/dl')
            
            with col2:
                sod = st.number_input('Sodium (mEq/L)', min_value=0, max_value=200, value=135,
                                    help='Enter sodium level in mEq/L')
                pot = st.number_input('Potassium (mEq/L)', min_value=0.0, max_value=10.0, value=4.0,
                                    help='Enter potassium level in mEq/L')
                hemo = st.number_input('Hemoglobin (gms)', min_value=0.0, max_value=20.0, value=12.0,
                                     help='Enter hemoglobin in gms')
                pcv = st.number_input('Packed Cell Volume (%)', min_value=0, max_value=60, value=40,
                                    help='Enter packed cell volume percentage')
                wbcc = st.number_input('White Blood Cell Count (cells/cumm)', min_value=0, max_value=50000, value=8000,
                                     help='Enter white blood cell count in cells/cumm')
                rbcc = st.number_input('Red Blood Cell Count (millions/cmm)', min_value=0.0, max_value=8.0, value=4.5,
                                     help='Enter red blood cell count in millions/cmm')
        
        with tab3:
            col1, col2 = st.columns(2)
            with col1:
                rbc = st.radio('Red Blood Cells', ['normal', 'abnormal'], help='Select red blood cells condition')
                pc = st.radio('Pus Cell', ['normal', 'abnormal'], help='Select pus cell condition')
                pcc = st.radio('Pus Cell Clumps', ['present', 'notpresent'], help='Select if pus cell clumps are present')
                ba = st.radio('Bacteria', ['present', 'notpresent'], help='Select if bacteria are present')
            
            with col2:
                htn = st.radio('Hypertension', ['yes', 'no'], help='Select if patient has hypertension')
                dm = st.radio('Diabetes Mellitus', ['yes', 'no'], help='Select if patient has diabetes mellitus')
                cad = st.radio('Coronary Artery Disease', ['yes', 'no'], help='Select if patient has coronary artery disease')

            st.markdown("---")
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                predict_button = st.button('Predict', use_container_width=True)

            if predict_button:
                rbc_num = 1 if rbc == 'abnormal' else 0
                pc_num = 1 if pc == 'abnormal' else 0
                pcc_num = 1 if pcc == 'present' else 0
                ba_num = 1 if ba == 'present' else 0
                htn_num = 1 if htn == 'yes' else 0
                dm_num = 1 if dm == 'yes' else 0
                cad_num = 1 if cad == 'yes' else 0
                appet_num = 1 if appet == 'poor' else 0
                pe_num = 1 if pe == 'yes' else 0
                ane_num = 1 if ane == 'yes' else 0

                input_data = np.array([[
                    int(age),              # age - Int64
                    int(bp),               # bp - Int64
                    int(sg * 1000),        # sg - int64 (converting from float to int by multiplying by 1000)
                    int(al),               # al - int64
                    int(su),               # su - int64
                    int(rbc_num),          # rbc - int64
                    int(pc_num),           # pc - int64
                    int(pcc_num),          # pcc - int64
                    int(ba_num),           # ba - int64
                    int(bgr),              # bgr - Int64
                    int(bu),               # bu - Int64
                    float(sc),             # sc - float64
                    int(sod),              # sod - Int64
                    float(pot),            # pot - float64
                    float(hemo),           # hemo - float64
                    int(pcv),              # pcv - Int64
                    float(wbcc),           # wbcc - float64
                    float(rbcc),           # rbcc - float64
                    int(htn_num),          # htn - int64
                    int(dm_num),           # dm - int64
                    int(cad_num),          # cad - int64
                    int(appet_num),        # appet - int64
                    int(pe_num),           # pe - int64
                    int(ane_num),          # ane - int64
                ]])

                try:
                    prediction = model.predict(input_data)
                    prediction_proba = model.predict_proba(input_data)

                    st.markdown("---")
                    st.subheader("🔍 Prediction Result")
                    
                    result_col1, result_col2 = st.columns([2, 1])
                    with result_col1:
                        if prediction[0] == 1:
                            st.error('⚠️ High Risk: The patient is likely to have Chronic Kidney Disease')
                        else:
                            st.success('✅ Low Risk: The patient is likely to be healthy')
                    
                    with result_col2:
                        st.metric(
                            label="Risk Probability",
                            value=f"{prediction_proba[0][1]:.1%}"
                        )

                except Exception as e:
                    st.error(f"Error making prediction: {str(e)}")

    except FileNotFoundError:
        st.error("Error: Model file not found. Please ensure the model file exists in the correct location.")

if __name__ == '__main__':
    main()