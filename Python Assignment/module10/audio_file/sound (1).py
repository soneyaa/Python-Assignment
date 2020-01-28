import winsound
n=int(input("Enter number"))
l=len(str(n))
#d1={0:winsound.PlaySound('0.wav',winsound.SND_FILENAME),1:winsound.PlaySound('1.wav',winsound.SND_FILENAME),2:winsound.PlaySound('2.wav',winsound.SND_FILENAME),3:winsound.PlaySound('3.wav',winsound.SND_FILENAME),4:winsound.PlaySound('4.wav',winsound.SND_FILENAME),5:winsound.PlaySound('5.wav',winsound.SND_FILENAME),6:winsound.PlaySound('6.wav',winsound.SND_FILENAME),7:winsound.PlaySound('7.wav',winsound.SND_FILENAME),8:winsound.PlaySound('8.wav',winsound.SND_FILENAME),9:winsound.PlaySound('9.wav',winsound.SND_FILENAME)}
#d2={10:winsound.PlaySound('10.wav',winsound.SND_FILENAME),11:winsound.PlaySound('11.wav',winsound.SND_FILENAME),12:winsound.PlaySound('12.wav',winsound.SND_FILENAME),13:winsound.PlaySound('13.wav',winsound.SND_FILENAME),14:winsound.PlaySound('14.wav',winsound.SND_FILENAME),15:winsound.PlaySound('15.wav',winsound.SND_FILENAME),16:winsound.PlaySound('16.wav',winsound.SND_FILENAME),17:winsound.PlaySound('17.wav',winsound.SND_FILENAME),18:winsound.PlaySound('18.wav',winsound.SND_FILENAME),19:winsound.PlaySound('19.wav',winsound.SND_FILENAME),20:winsound.PlaySound('20.wav',winsound.SND_FILENAME),30:winsound.PlaySound('30.wav',winsound.SND_FILENAME),40:winsound.PlaySound('40.wav',winsound.SND_FILENAME),50:winsound.PlaySound('50.wav',winsound.SND_FILENAME),60:winsound.PlaySound('60.wav',winsound.SND_FILENAME),70:winsound.PlaySound('70.wav',winsound.SND_FILENAME),80:winsound.PlaySound('80.wav',winsound.SND_FILENAME),90:winsound.PlaySound('90.wav',winsound.SND_FILENAME)}
c=['0.wav','1.wav','2.wav','3.wav','4.wav','5.wav','6.wav','7.wav','8.wav','9.wav']
c1=['10.wav','11.wav','12.wav','13.wav','14.wav','15.wav','16.wav','17.wav','18.wav','19.wav','20.wav','30.wav','40.wav','50.wav','60.wav','70.wav','80.wav','90.wav']
c2=[10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]
if l==1:
    winsound.PlaySound(c[n],winsound.SND_FILENAME)
    print(c[n])
elif l==2:
    if n in c2:
        winsound.PlaySound(c1[c2.index(n)],winsound.SND_FILENAME)
    else:
        a=n//10
        a=a*10
        winsound.PlaySound(c1[c2.index(a)],winsound.SND_FILENAME)
        r=n%10
        if r!=0:
            winsound.PlaySound(c[r],winsound.SND_FILENAME)
else:
    print("we can download more .wav files to get sound for more numbers")
