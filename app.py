import streamlit as st
from Api import func
from DataType import Fraction
from DataType import Vector

url='https://github.com/praweenkr01/fraction_and_vector_calculator'
st.markdown(f'''
<a href={url}><button style="background-color:GreenYellow;">GitHub Link</button></a>
''',unsafe_allow_html=True)

st.title('Fraction Calculator')
oper=st.selectbox('Select Features to Check',['Arithematic Operation','Maximum','Minimum','Greatest common divisor','Least common multiple',
'Are Like Fraction','Reciprocal'])
tokens=st.text_input('Enter your Fractions or Equation')
#submit button
if st.button('Submit'):
    res=None
    if oper=='Arithematic Operation':
        try:
            res=func(tokens)
        except:
            res=None
    elif oper=='Reciprocal':
            try:
                res=Fraction(tokens).reciprocal()
            except:
                res=None
    else:
        tokens=tokens.split(',')
        fcn=[]
        ret=False
        for f in tokens:
            try:
                fcn.append(Fraction(f))
            except:
                ret=True
                break
        if ret:
            res=None
        elif oper=='Maximum':
            try:
                res=Fraction.max(fcn)
            except:
                res=None

        elif oper=='Minimum':
            try:
                res=Fraction.min(fcn)
            except:
                res=None
        elif oper=='Are Like Fraction':
            try:
                res=Fraction.are_like_fraction(fcn)
            except:
                res=None
        else:
            num = []
            deno = []
            for f in fcn:
                num.append(f.num)
                deno.append(f.deno)
            def hcf(nm):
                a=nm[0]
                while nm:
                    b=nm.pop()
                    while a % b != 0:
                        rem = a % b
                        a = b
                        b = rem
                    a=b
                    if a==1:
                        return 1

            def lcm(nm):
                def hc(a,b):
                    while a % b != 0:
                        rem = a % b
                        a = b
                        b = rem
                    return b
                a=nm[0]
                # b=nm.pop()
                while nm:
                    b=nm.pop()
                    a=a*b/hc(a,b)
                return a

            if oper=='Greatest common divisor':
                try:
                    u=hcf(num)
                    d=lcm(deno)
                    res=Fraction(u,d)
                except:
                    res=None

            elif oper=='Least common multiple':
                try:
                    u=lcm(num)
                    d=hcf(deno)
                    res=Fraction(u,d)
                except:
                    res=None
    if res is None:
        st.error('check')

    else:
        st.success('result : '+str(res))
        st.info('result : '+str(float(res)))

##Now the vector calculation

st.title('Vector Calculation')
op=st.selectbox('Select the operation to be performed',['Magnitude','Direction Cosine','Angle With x','Angle with y','Angle With z','Unit Vector Direction',
                                                        'Dot Product','Cross Product','Addition','Projection','Collinear','Angle Between Vectors','Check Perpendicular'])
aset={'Dot Product','Cross Product','Addition','Projection','Collinear','Angle Between Vectors','Check Perpendicular'}


st.write('Write the value of the coordinate')
cols=st.columns(3)
# x,y,z=None,None,None
# x2,y2,z2=None,None,None
with cols[0]:
    x = st.text_input('x',value='0')
with cols[1]:
    y = st.text_input('y',value='0')
with cols[2]:
    z = st.text_input('z',value='0')
v1=Vector(x,y,z)

if op in aset:
    st.write('Write the value of the coordinate')
    col = st.columns(3)
    with col[0]:
        x2 = st.text_input('x2',value='0')
    with col[1]:
        y2 = st.text_input('y2',value='0')
    with col[2]:
        z2 = st.text_input('z2',value='0')
try:
    v2=Vector(x2,y2,z2)
except:
    pass


res=None

if op=='Magnitude':
    try:
        res=v1.magnitude()
    except:
        res = None

elif op=='Direction Cosine':
    try:
        res=Vector.direction_cosine(v1)
    except:
        res = None
elif op=='Angle With x':
    try:
        res=v1.angle_with_x_rad()
    except:
        res = None
elif op=='Angle with y':
    try:
        res=v1.angle_with_y_rad()
    except:
        res = None
elif op=='Angle With z':
    try:
        res=v1.angle_with_z_rad()
    except:
        res = None
elif op=='Unit Vector Direction':
    try:
        res=v1.unit_vector_direction()
    except:
        res = None
elif op=='Dot Product':
    try:
        res=v1.dot_product(v2)
    except:
        res = None
elif op=='Cross Product':
    try:
        res=v1*v2
    except:
        res=None
elif op=='Addition':
    try:
        res=v1+v2
    except:
        res = None
elif op=='Projection':
    try:
        res=v1.projection(v2)
    except:
        res = None
elif op=='Collinear':
    try:
        res=v1.are_collinear(v2)
    except:
        res = None
elif op=='Angle Between Vectors':
    try:
        res=v1.angle_between_vector(v2)
    except:
        res = None
elif op=='Check Perpendicular':
    try:
        res=v1.are_perpendicular(v2)
    except:
        res = None

if st.button('Submits'):
    if res is None:
        st.error('Error somewhere..')
    else:
        st.success(res)
