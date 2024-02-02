import streamlit as st
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
# empty1,con1,empty2 = st.columns([0.3,1.0,0.3])
col1, col2, col3 = st.columns(3)

st.title('Dataset Distillation with Distribution Matching')
st.markdown("---")

classes = st.radio("Class", ["Whole", "Plane", "Car", "Bird", "Cat", "Deer", "Dog", "Frog", "Horse", "Ship", "Truck"])
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

iter = st.slider("Iteration", 0, 20000, 0, 2000)
# st.markdown("<h1 style='text-align: center; color: black;'>Iteration {}</h1>".format(iter), unsafe_allow_html=True)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.header('Iteration {}'.format(iter))
    if classes == "Whole":
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(img, caption='{}'.format(classes),use_column_width = True)
    elif classes == "Plane":
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        cropped_image = img.crop((0, 0, 342, 36))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(cropped_image, caption='{}'.format(classes),use_column_width = True)
    elif classes == "Car":
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        cropped_image = img.crop((0, 34, 342, 34*2+2))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(cropped_image, caption='{}'.format(classes),use_column_width = True)
    elif classes == "Bird":
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        cropped_image = img.crop((0, 34 * 2, 342, 34*3+2))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(cropped_image, caption='{}'.format(classes),use_column_width = True)
    elif classes == "Cat":
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        cropped_image = img.crop((0, 34*3, 342, 34*4+2))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(cropped_image, caption='{}'.format(classes),use_column_width = True)
    elif classes == "Deer":
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        cropped_image = img.crop((0, 34*4, 342, 34*5+2))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(cropped_image, caption='{}'.format(classes),use_column_width = True)
    elif classes == "Dog":
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        cropped_image = img.crop((0, 34*5, 342, 34*6+2))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(cropped_image, caption='{}'.format(classes),use_column_width = True)
    elif classes == "Frog":
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        cropped_image = img.crop((0, 34*6, 342, 34*7+2))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(cropped_image, caption='{}'.format(classes),use_column_width = True)
    elif classes == "Horse":
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        cropped_image = img.crop((0, 34*7, 342, 34*8+2))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(cropped_image, caption='{}'.format(classes),use_column_width = True)
    elif classes == "Ship":
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        cropped_image = img.crop((0, 34*8, 342, 34*9+2))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(cropped_image, caption='{}'.format(classes),use_column_width = True)
    else:
        img = Image.open('vis_DM_CIFAR10_ConvNet_10ipc_exp0_iter{}.png'.format(iter))
        cropped_image = img.crop((0, 34*9, 342, 34*10+2))
        st.write("<style>img {width: 100%; height:100%}</style>", unsafe_allow_html=True)
        st.image(cropped_image, caption='{}'.format(classes),use_column_width = True)
