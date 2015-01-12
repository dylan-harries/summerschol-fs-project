Block SPINFO
     1   FlexibleSUSY
     2   1.0.3
Block MODSEL                 # Select model
#   12    1000                # DRbar parameter output scale (GeV)
Block FlexibleSUSY
    0   1.000000000e-04      # precision goal
    1   0                    # max. iterations (0 = automatic)
    2   0                    # algorithm (0 = two_scale, 1 = lattice)
    3   0                    # calculate SM pole masses
    4   2                    # pole mass loop order
    5   2                    # EWSB loop order
    6   2                    # beta-functions loop order
    7   1                    # threshold corrections loop order
    8   1                    # Higgs 2-loop corrections O(alpha_t alpha_s)
    9   1                    # Higgs 2-loop corrections O(alpha_b alpha_s)
   10   1                    # Higgs 2-loop corrections O(alpha_t^2 + alpha_t alpha_b + alpha_b^2)
   11   1                    # Higgs 2-loop corrections O(alpha_tau^2)
Block SMINPUTS
     1     1.27934000E+02   # alpha^(-1) SM MSbar(MZ)
     2     1.16637000E-05   # G_Fermi
     3     1.17600000E-01   # alpha_s(MZ) SM MSbar
     4     9.11876000E+01   # MZ(pole)
     5     4.20000000E+00   # mb(mb) SM MSbar
     6     1.73300000E+02   # mtop(pole)
     7     1.77700000E+00   # mtau(pole)
     8                  0   # mnu3(pole)
    11     5.02667588E-04   # melectron(pole)
    12                  0   # mnu1(pole)
    13     1.03935706E-01   # mmuon(pole)
    14                  0   # mnu2(pole)
    21     4.76052706E-03   # md
    22     2.40534062E-03   # mu
    23     1.04230487E-01   # ms
    24     1.27183378E+00   # mc
Block MINPAR
     1     2.00000000E+03   # m0
     2     2.00000000E+03   # m12
     3     6.00000000E+00   # TanBeta
     5     0.00000000E+00   # Azero
Block EXTPAR
    61     1.00000000E-01   # LambdaInput
    62     2.00000000E-01   # KappaInput
    63     1.00000000E+04   # muPrimeInput
    64     1.00000000E+04   # BmuPrimeInput
    65     8.00000000E+03   # vSInput
    66     3.00000000E-01   # Lambda12Input
Block gauge Q= 2.31538541E+03
     1     3.64905384E-01   # gY
     2     6.38256510E-01   # g2
     3     1.02226889E+00   # g3
     4     4.75288061E-01   # gN
Block Yu Q= 2.31538541E+03
  1  1     7.30439056E-06   # Yu(1,1)
  1  2     0.00000000E+00   # Yu(1,2)
  1  3     0.00000000E+00   # Yu(1,3)
  2  1     0.00000000E+00   # Yu(2,1)
  2  2     3.33848187E-03   # Yu(2,2)
  2  3     0.00000000E+00   # Yu(2,3)
  3  1     0.00000000E+00   # Yu(3,1)
  3  2     0.00000000E+00   # Yu(3,2)
  3  3     8.74176100E-01   # Yu(3,3)
Block Yd Q= 2.31538541E+03
  1  1     8.29323524E-05   # Yd(1,1)
  1  2     0.00000000E+00   # Yd(1,2)
  1  3     0.00000000E+00   # Yd(1,3)
  2  1     0.00000000E+00   # Yd(2,1)
  2  2     1.81578291E-03   # Yd(2,2)
  2  3     0.00000000E+00   # Yd(2,3)
  3  1     0.00000000E+00   # Yd(3,1)
  3  2     0.00000000E+00   # Yd(3,2)
  3  3     8.10336771E-02   # Yd(3,3)
Block Ye Q= 2.31538541E+03
  1  1     1.67550126E-05   # Ye(1,1)
  1  2     0.00000000E+00   # Ye(1,2)
  1  3     0.00000000E+00   # Ye(1,3)
  2  1     0.00000000E+00   # Ye(2,1)
  2  2     3.46440757E-03   # Ye(2,2)
  2  3     0.00000000E+00   # Ye(2,3)
  3  1     0.00000000E+00   # Ye(3,1)
  3  2     0.00000000E+00   # Ye(3,2)
  3  3     5.96437177E-02   # Ye(3,3)
Block Te Q= 2.31538541E+03
  1  1    -1.93769200E-02   # TYe(1,1)
  1  2     0.00000000E+00   # TYe(1,2)
  1  3     0.00000000E+00   # TYe(1,3)
  2  1     0.00000000E+00   # TYe(2,1)
  2  2    -4.00650660E+00   # TYe(2,2)
  2  3     0.00000000E+00   # TYe(2,3)
  3  1     0.00000000E+00   # TYe(3,1)
  3  2     0.00000000E+00   # TYe(3,2)
  3  3    -6.88310146E+01   # TYe(3,3)
Block Td Q= 2.31538541E+03
  1  1    -3.80753904E-01   # TYd(1,1)
  1  2     0.00000000E+00   # TYd(1,2)
  1  3     0.00000000E+00   # TYd(1,3)
  2  1     0.00000000E+00   # TYd(2,1)
  2  2    -8.33649354E+00   # TYd(2,2)
  2  3     0.00000000E+00   # TYd(2,3)
  3  1     0.00000000E+00   # TYd(3,1)
  3  2     0.00000000E+00   # TYd(3,2)
  3  3    -3.44521890E+02   # TYd(3,3)
Block Tu Q= 2.31538541E+03
  1  1    -2.57849439E-02   # TYu(1,1)
  1  2     0.00000000E+00   # TYu(1,2)
  1  3     0.00000000E+00   # TYu(1,3)
  2  1     0.00000000E+00   # TYu(2,1)
  2  2    -1.17849902E+01   # TYu(2,2)
  2  3     0.00000000E+00   # TYu(2,3)
  3  1     0.00000000E+00   # TYu(3,1)
  3  2     0.00000000E+00   # TYu(3,2)
  3  3    -2.20520208E+03   # TYu(3,3)
Block MSQ2 Q= 2.31538541E+03
  1  1     9.93907649E+06   # mq2(1,1)
  1  2     0.00000000E+00   # mq2(1,2)
  1  3     0.00000000E+00   # mq2(1,3)
  2  1     0.00000000E+00   # mq2(2,1)
  2  2     9.93900737E+06   # mq2(2,2)
  2  3     0.00000000E+00   # mq2(2,3)
  3  1     0.00000000E+00   # mq2(3,1)
  3  2     0.00000000E+00   # mq2(3,2)
  3  3     6.59045680E+06   # mq2(3,3)
Block MSE2 Q= 2.31538541E+03
  1  1     4.02172709E+06   # me2(1,1)
  1  2     0.00000000E+00   # me2(1,2)
  1  3     0.00000000E+00   # me2(1,3)
  2  1     0.00000000E+00   # me2(2,1)
  2  2     4.02163343E+06   # me2(2,2)
  2  3     0.00000000E+00   # me2(2,3)
  3  1     0.00000000E+00   # me2(3,1)
  3  2     0.00000000E+00   # me2(3,2)
  3  3     3.99396967E+06   # me2(3,3)
Block MSL2 Q= 2.31538541E+03
  1  1     5.19338241E+06   # ml2(1,1)
  1  2     0.00000000E+00   # ml2(1,2)
  1  3     0.00000000E+00   # ml2(1,3)
  2  1     0.00000000E+00   # ml2(2,1)
  2  2     5.19333603E+06   # ml2(2,2)
  2  3     0.00000000E+00   # ml2(2,3)
  3  1     0.00000000E+00   # ml2(3,1)
  3  2     0.00000000E+00   # ml2(3,2)
  3  3     5.17963984E+06   # ml2(3,3)
Block MSU2 Q= 2.31538541E+03
  1  1     9.68892538E+06   # mu2(1,1)
  1  2     0.00000000E+00   # mu2(1,2)
  1  3     0.00000000E+00   # mu2(1,3)
  2  1     0.00000000E+00   # mu2(2,1)
  2  2     9.68881602E+06   # mu2(2,2)
  2  3     0.00000000E+00   # mu2(2,3)
  3  1     0.00000000E+00   # mu2(3,1)
  3  2     0.00000000E+00   # mu2(3,2)
  3  3     2.92170355E+06   # mu2(3,3)
Block MSD2 Q= 2.31538541E+03
  1  1     9.36073031E+06   # md2(1,1)
  1  2     0.00000000E+00   # md2(1,2)
  1  3     0.00000000E+00   # md2(1,3)
  2  1     0.00000000E+00   # md2(2,1)
  2  2     9.36070004E+06   # md2(2,2)
  2  3     0.00000000E+00   # md2(2,3)
  3  1     0.00000000E+00   # md2(3,1)
  3  2     0.00000000E+00   # md2(3,2)
  3  3     9.30350578E+06   # md2(3,3)
Block MSOFT Q= 2.31538541E+03
    21     5.47529783E+06   # mHd2
    22     1.69075014E+06   # mHu2
    23    -4.74880605E+06   # ms2
    24     5.19338241E+06   # mHp2
    25     4.65322073E+06   # mHpbar2
     1     3.33975451E+02   # MassB
     2     5.89581650E+02   # MassWB
     3     1.46170384E+03   # MassG
     4     3.40936547E+02   # MassBp
Block mHdInert2 Q= 2.31538541E+03
  1  1     4.48375652E+06   # mH1I2(1,1)
  1  2     0.00000000E+00   # mH1I2(1,2)
  2  1     0.00000000E+00   # mH1I2(2,1)
  2  2     4.48375652E+06   # mH1I2(2,2)
Block mHuInert2 Q= 2.31538541E+03
  1  1     4.12451280E+06   # mH2I2(1,1)
  1  2     0.00000000E+00   # mH2I2(1,2)
  2  1     0.00000000E+00   # mH2I2(2,1)
  2  2     4.12451280E+06   # mH2I2(2,2)
Block mX2 Q= 2.31538541E+03
  1  1     8.43401908E+06   # mDx2(1,1)
  1  2     0.00000000E+00   # mDx2(1,2)
  1  3     0.00000000E+00   # mDx2(1,3)
  2  1     0.00000000E+00   # mDx2(2,1)
  2  2     8.43401908E+06   # mDx2(2,2)
  2  3     0.00000000E+00   # mDx2(2,3)
  3  1     0.00000000E+00   # mDx2(3,1)
  3  2     0.00000000E+00   # mDx2(3,2)
  3  3     8.43401908E+06   # mDx2(3,3)
Block mXBar2 Q= 2.31538541E+03
  1  1     8.19564576E+06   # mDxbar2(1,1)
  1  2     0.00000000E+00   # mDxbar2(1,2)
  1  3     0.00000000E+00   # mDxbar2(1,3)
  2  1     0.00000000E+00   # mDxbar2(2,1)
  2  2     8.19564576E+06   # mDxbar2(2,2)
  2  3     0.00000000E+00   # mDxbar2(2,3)
  3  1     0.00000000E+00   # mDxbar2(3,1)
  3  2     0.00000000E+00   # mDxbar2(3,2)
  3  3     8.19564576E+06   # mDxbar2(3,3)
Block msInert2 Q= 2.31538541E+03
  1  1     4.56720738E+06   # msI2(1,1)
  1  2     0.00000000E+00   # msI2(1,2)
  2  1     0.00000000E+00   # msI2(2,1)
  2  2     4.56720738E+06   # msI2(2,2)
Block HMIX Q= 2.31538541E+03
   102     4.16161240E+01   # vd
   103     2.37331869E+02   # vu
Block ESIXRUN Q= 2.31538541E+03
    11     7.99999656E+03   # vs
     1     1.01137521E-01   # Lambdax
     2     1.01407065E+02   # TLambdax
     0     9.99999745E+03   # MuPr
   101     1.00027533E+04   # BMuPr
Block ESIXKAPPA Q= 2.31538541E+03
  1  1     4.93579473E-01   # Kappa(1,1)
  1  2     0.00000000E+00   # Kappa(1,2)
  1  3     0.00000000E+00   # Kappa(1,3)
  2  1     0.00000000E+00   # Kappa(2,1)
  2  2     4.93579473E-01   # Kappa(2,2)
  2  3     0.00000000E+00   # Kappa(2,3)
  3  1     0.00000000E+00   # Kappa(3,1)
  3  2     0.00000000E+00   # Kappa(3,2)
  3  3     4.93579473E-01   # Kappa(3,3)
Block ESIXTKAPPA Q= 2.31538541E+03
  1  1    -1.32328523E+03   # TKappa(1,1)
  1  2     0.00000000E+00   # TKappa(1,2)
  1  3     0.00000000E+00   # TKappa(1,3)
  2  1     0.00000000E+00   # TKappa(2,1)
  2  2    -1.32328523E+03   # TKappa(2,2)
  2  3     0.00000000E+00   # TKappa(2,3)
  3  1     0.00000000E+00   # TKappa(3,1)
  3  2     0.00000000E+00   # TKappa(3,2)
  3  3    -1.32328523E+03   # TKappa(3,3)
Block ESIXLAMBDA Q= 2.31538541E+03
  1  1     3.63720424E-01   # Lambda12(1,1)
  1  2     0.00000000E+00   # Lambda12(1,2)
  2  1     0.00000000E+00   # Lambda12(2,1)
  2  2     3.63720424E-01   # Lambda12(2,2)
Block ESIXTLAMBDA Q= 2.31538541E+03
  1  1    -1.18085217E+01   # TLambda12(1,1)
  1  2     0.00000000E+00   # TLambda12(1,2)
  2  1     0.00000000E+00   # TLambda12(2,1)
  2  2    -1.18085217E+01   # TLambda12(2,2)
Block MASS
   1000021     1.74358456E+03   # Glu
        24     8.04040000E+01   # VWm
   1000091     9.95701969E+03   # ChaP
        31     3.00670146E+03   # VZp
   1000089     0.00000000E+00   # FSI(1)
   1000090     0.00000000E+00   # FSI(2)
   1000092    -9.95667002E+03   # ChiP(1)
   1000094     9.95667002E+03   # ChiP(2)
   1000024     5.37125578E+02   # Cha(1)
   1000037     6.72613435E+02   # Cha(2)
        37     1.79614863E+03   # Hpm(2)
        92     1.01065297E+04   # SHp0(1)
        94     1.03084118E+04   # SHp0(2)
        91     1.00971677E+04   # SHpp(1)
        93     1.03000241E+04   # SHpp(2)
        89     3.00577989E+03   # SSI0(1)
        90     3.00577989E+03   # SSI0(2)
   1000085     2.07932800E+03   # ChaI(1)
   1000086     2.07932800E+03   # ChaI(2)
        25     1.25475385E+02   # hh(1)
        35     1.79448514E+03   # hh(2)
        45     3.05756412E+03   # hh(3)
   1000012     2.64535748E+03   # Sv(1)
   1000014     2.64805358E+03   # Sv(2)
   1000016     2.64806271E+03   # Sv(3)
        36     1.79424475E+03   # Ah(3)
        51     2.90905298E+03   # FDX(1)
        52     2.90905298E+03   # FDX(2)
        53     2.90905298E+03   # FDX(3)
   1000081    -2.07898330E+03   # ChiI(1)
   1000082    -2.07898330E+03   # ChiI(2)
   1000083     2.07898330E+03   # ChiI(3)
   1000084     2.07898330E+03   # ChiI(4)
        82     2.46154071E+03   # SHI0(1)
        86     2.46154071E+03   # SHI0(2)
        84     2.58456955E+03   # SHI0(3)
        88     2.58456955E+03   # SHI0(4)
        81     2.46449853E+03   # SHIp(1)
        85     2.46449853E+03   # SHIp(2)
        83     2.58562700E+03   # SHIp(3)
        87     2.58562700E+03   # SHIp(4)
   1000022     3.31772442E+02   # Chi(1)
   1000023     5.39929548E+02   # Chi(2)
   1000025    -5.83098855E+02   # Chi(3)
   1000035     6.73232419E+02   # Chi(4)
   1000045    -2.84508699E+03   # Chi(5)
   1000055     3.16920484E+03   # Chi(6)
   1000001     2.75041182E+03   # Sd(1)
   1000003     3.33328922E+03   # Sd(2)
   1000005     3.33330026E+03   # Sd(3)
   2000001     3.36607482E+03   # Sd(4)
   2000003     3.37505089E+03   # Sd(5)
   2000005     3.37505549E+03   # Sd(6)
   1000011     2.21206053E+03   # Se(1)
   1000013     2.21852546E+03   # Se(2)
   1000015     2.21854732E+03   # Se(3)
   2000011     2.64680225E+03   # Se(4)
   2000013     2.64949108E+03   # Se(5)
   2000015     2.64950017E+03   # Se(6)
   1000002     1.95536310E+03   # Su(1)
   1000004     2.76125516E+03   # Su(2)
   1000006     3.29087941E+03   # Su(3)
   2000002     3.29089929E+03   # Su(4)
   2000004     3.33253649E+03   # Su(5)
   2000006     3.33254494E+03   # Su(6)
   1000051     2.61617319E+03   # SDX(1)
   2000051     2.61617319E+03   # SDX(2)
   1000052     2.61617319E+03   # SDX(3)
   2000052     4.69641117E+03   # SDX(4)
   1000053     4.69641117E+03   # SDX(5)
   2000053     4.69641117E+03   # SDX(6)
Block INHMIX
  1  1    -9.66948296E-01   # UHI0(1,1)
  1  2    -0.00000000E+00   # UHI0(1,2)
  1  3     2.54972535E-01   # UHI0(1,3)
  1  4    -0.00000000E+00   # UHI0(1,4)
  2  1    -0.00000000E+00   # UHI0(2,1)
  2  2     9.66948296E-01   # UHI0(2,2)
  2  3    -0.00000000E+00   # UHI0(2,3)
  2  4    -2.54972535E-01   # UHI0(2,4)
  3  1     2.54972535E-01   # UHI0(3,1)
  3  2     0.00000000E+00   # UHI0(3,2)
  3  3     9.66948296E-01   # UHI0(3,3)
  3  4     0.00000000E+00   # UHI0(3,4)
  4  1     0.00000000E+00   # UHI0(4,1)
  4  2    -2.54972535E-01   # UHI0(4,2)
  4  3     0.00000000E+00   # UHI0(4,3)
  4  4    -9.66948296E-01   # UHI0(4,4)
Block ICHMIX
  1  1    -9.64039404E-01   # UHIp(1,1)
  1  2    -0.00000000E+00   # UHIp(1,2)
  1  3    -2.65759341E-01   # UHIp(1,3)
  1  4    -0.00000000E+00   # UHIp(1,4)
  2  1    -0.00000000E+00   # UHIp(2,1)
  2  2    -9.64039404E-01   # UHIp(2,2)
  2  3    -0.00000000E+00   # UHIp(2,3)
  2  4    -2.65759341E-01   # UHIp(2,4)
  3  1     2.65759341E-01   # UHIp(3,1)
  3  2     0.00000000E+00   # UHIp(3,2)
  3  3    -9.64039404E-01   # UHIp(3,3)
  3  4     0.00000000E+00   # UHIp(3,4)
  4  1     0.00000000E+00   # UHIp(4,1)
  4  2     2.65759341E-01   # UHIp(4,2)
  4  3     0.00000000E+00   # UHIp(4,3)
  4  4    -9.64039404E-01   # UHIp(4,4)
Block UHNPMIX
  1  1     1.30269788E-02   # UHp0(1,1)
  1  2     9.99915145E-01   # UHp0(1,2)
  2  1     9.99915145E-01   # UHp0(2,1)
  2  2    -1.30269788E-02   # UHp0(2,2)
Block UHPPMIX
  1  1    -1.57599108E-02   # UHpp(1,1)
  1  2     9.99875805E-01   # UHpp(1,2)
  2  1     9.99875805E-01   # UHpp(2,1)
  2  2     1.57599108E-02   # UHpp(2,2)
Block UMIX
  1  1    -5.47454729E-01   # Re(UM(1,1))
  1  2     8.36835300E-01   # Re(UM(1,2))
  2  1     8.36835300E-01   # Re(UM(2,1))
  2  2     5.47454729E-01   # Re(UM(2,2))
Block VMIX
  1  1    -6.08742399E-01   # Re(UP(1,1))
  1  2     7.93367942E-01   # Re(UP(1,2))
  2  1     7.93367942E-01   # Re(UP(2,1))
  2  2     6.08742399E-01   # Re(UP(2,2))
Block NMAMIX
  1  1    -1.72760265E-01   # ZA(1,1)
  1  2     9.84900709E-01   # ZA(1,2)
  1  3     1.11572633E-02   # ZA(1,3)
  2  1     3.12884246E-03   # ZA(2,1)
  2  2     1.18762849E-02   # ZA(2,2)
  2  3    -9.99924579E-01   # ZA(2,3)
  3  1     9.84958934E-01   # ZA(3,1)
  3  2     1.72712326E-01   # ZA(3,2)
  3  3     5.13334929E-03   # ZA(3,3)
Block DSQMIX
  1  1    -0.00000000E+00   # ZD(1,1)
  1  2     3.18686048E-18   # ZD(1,2)
  1  3    -9.99988556E-01   # ZD(1,3)
  1  4    -0.00000000E+00   # ZD(1,4)
  1  5    -5.31166338E-23   # ZD(1,5)
  1  6    -4.78411456E-03   # ZD(1,6)
  2  1    -0.00000000E+00   # ZD(2,1)
  2  2    -9.99999121E-01   # ZD(2,2)
  2  3    -0.00000000E+00   # ZD(2,3)
  2  4    -0.00000000E+00   # ZD(2,4)
  2  5    -1.32591026E-03   # ZD(2,5)
  2  6    -5.55111045E-16   # ZD(2,6)
  3  1    -9.99999998E-01   # ZD(3,1)
  3  2    -0.00000000E+00   # ZD(3,2)
  3  3    -0.00000000E+00   # ZD(3,3)
  3  4    -6.05662046E-05   # ZD(3,4)
  3  5    -0.00000000E+00   # ZD(3,5)
  3  6    -0.00000000E+00   # ZD(3,6)
  4  1     0.00000000E+00   # ZD(4,1)
  4  2     6.66126192E-16   # ZD(4,2)
  4  3     4.78411456E-03   # ZD(4,3)
  4  4     0.00000000E+00   # ZD(4,4)
  4  5    -1.11025824E-20   # ZD(4,5)
  4  6    -9.99988556E-01   # ZD(4,6)
  5  1     0.00000000E+00   # ZD(5,1)
  5  2     1.32591026E-03   # ZD(5,2)
  5  3     0.00000000E+00   # ZD(5,3)
  5  4     0.00000000E+00   # ZD(5,4)
  5  5    -9.99999121E-01   # ZD(5,5)
  5  6     7.24559135E-19   # ZD(5,6)
  6  1     6.05662046E-05   # ZD(6,1)
  6  2     0.00000000E+00   # ZD(6,2)
  6  3     0.00000000E+00   # ZD(6,3)
  6  4    -9.99999998E-01   # ZD(6,4)
  6  5     0.00000000E+00   # ZD(6,5)
  6  6     0.00000000E+00   # ZD(6,6)
Block ESIXZDX
  1  1     6.79932663E-01   # ZDX(1,1)
  1  2     0.00000000E+00   # ZDX(1,2)
  1  3     0.00000000E+00   # ZDX(1,3)
  1  4     7.33274555E-01   # ZDX(1,4)
  1  5     0.00000000E+00   # ZDX(1,5)
  1  6     0.00000000E+00   # ZDX(1,6)
  2  1     0.00000000E+00   # ZDX(2,1)
  2  2     6.79932663E-01   # ZDX(2,2)
  2  3     0.00000000E+00   # ZDX(2,3)
  2  4     0.00000000E+00   # ZDX(2,4)
  2  5     7.33274555E-01   # ZDX(2,5)
  2  6     0.00000000E+00   # ZDX(2,6)
  3  1     0.00000000E+00   # ZDX(3,1)
  3  2     0.00000000E+00   # ZDX(3,2)
  3  3     6.79932663E-01   # ZDX(3,3)
  3  4     0.00000000E+00   # ZDX(3,4)
  3  5     0.00000000E+00   # ZDX(3,5)
  3  6     7.33274555E-01   # ZDX(3,6)
  4  1     7.33274555E-01   # ZDX(4,1)
  4  2     0.00000000E+00   # ZDX(4,2)
  4  3     0.00000000E+00   # ZDX(4,3)
  4  4    -6.79932663E-01   # ZDX(4,4)
  4  5     0.00000000E+00   # ZDX(4,5)
  4  6     0.00000000E+00   # ZDX(4,6)
  5  1     0.00000000E+00   # ZDX(5,1)
  5  2     0.00000000E+00   # ZDX(5,2)
  5  3     7.33274555E-01   # ZDX(5,3)
  5  4     0.00000000E+00   # ZDX(5,4)
  5  5     0.00000000E+00   # ZDX(5,5)
  5  6    -6.79932663E-01   # ZDX(5,6)
  6  1     0.00000000E+00   # ZDX(6,1)
  6  2     7.33274555E-01   # ZDX(6,2)
  6  3     0.00000000E+00   # ZDX(6,3)
  6  4     0.00000000E+00   # ZDX(6,4)
  6  5    -6.79932663E-01   # ZDX(6,5)
  6  6     0.00000000E+00   # ZDX(6,6)
Block ESIXZXL
  1  1     0.00000000E+00   # Re(ZDXL(1,1))
  1  2     0.00000000E+00   # Re(ZDXL(1,2))
  1  3     1.00000000E+00   # Re(ZDXL(1,3))
  2  1     0.00000000E+00   # Re(ZDXL(2,1))
  2  2     1.00000000E+00   # Re(ZDXL(2,2))
  2  3     0.00000000E+00   # Re(ZDXL(2,3))
  3  1     1.00000000E+00   # Re(ZDXL(3,1))
  3  2     0.00000000E+00   # Re(ZDXL(3,2))
  3  3     0.00000000E+00   # Re(ZDXL(3,3))
Block ESIXZXR
  1  1     0.00000000E+00   # Re(ZDXR(1,1))
  1  2     0.00000000E+00   # Re(ZDXR(1,2))
  1  3     1.00000000E+00   # Re(ZDXR(1,3))
  2  1     0.00000000E+00   # Re(ZDXR(2,1))
  2  2     1.00000000E+00   # Re(ZDXR(2,2))
  2  3     0.00000000E+00   # Re(ZDXR(2,3))
  3  1     1.00000000E+00   # Re(ZDXR(3,1))
  3  2     0.00000000E+00   # Re(ZDXR(3,2))
  3  3     0.00000000E+00   # Re(ZDXR(3,3))
Block SELMIX
  1  1     0.00000000E+00   # ZE(1,1)
  1  2     0.00000000E+00   # ZE(1,2)
  1  3     3.74459429E-03   # ZE(1,3)
  1  4     0.00000000E+00   # ZE(1,4)
  1  5     0.00000000E+00   # ZE(1,5)
  1  6     9.99992989E-01   # ZE(1,6)
  2  1     0.00000000E+00   # ZE(2,1)
  2  2     2.19138652E-04   # ZE(2,2)
  2  3     0.00000000E+00   # ZE(2,3)
  2  4     0.00000000E+00   # ZE(2,4)
  2  5     9.99999976E-01   # ZE(2,5)
  2  6     0.00000000E+00   # ZE(2,6)
  3  1     1.05985342E-06   # ZE(3,1)
  3  2     0.00000000E+00   # ZE(3,2)
  3  3     0.00000000E+00   # ZE(3,3)
  3  4     1.00000000E+00   # ZE(3,4)
  3  5     0.00000000E+00   # ZE(3,5)
  3  6     0.00000000E+00   # ZE(3,6)
  4  1     0.00000000E+00   # ZE(4,1)
  4  2     0.00000000E+00   # ZE(4,2)
  4  3     9.99992989E-01   # ZE(4,3)
  4  4     0.00000000E+00   # ZE(4,4)
  4  5     0.00000000E+00   # ZE(4,5)
  4  6    -3.74459429E-03   # ZE(4,6)
  5  1     0.00000000E+00   # ZE(5,1)
  5  2     9.99999976E-01   # ZE(5,2)
  5  3     0.00000000E+00   # ZE(5,3)
  5  4     0.00000000E+00   # ZE(5,4)
  5  5    -2.19138652E-04   # ZE(5,5)
  5  6     0.00000000E+00   # ZE(5,6)
  6  1     1.00000000E+00   # ZE(6,1)
  6  2     0.00000000E+00   # ZE(6,2)
  6  3     0.00000000E+00   # ZE(6,3)
  6  4    -1.05985342E-06   # ZE(6,4)
  6  5     0.00000000E+00   # ZE(6,5)
  6  6     0.00000000E+00   # ZE(6,6)
Block ESIXZSI
  1  1     1.00000000E+00   # Re(ZFSI(1,1))
  1  2     0.00000000E+00   # Re(ZFSI(1,2))
  2  1     0.00000000E+00   # Re(ZFSI(2,1))
  2  2     1.00000000E+00   # Re(ZFSI(2,2))
Block NMHMIX
  1  1    -1.73962192E-01   # ZH(1,1)
  1  2    -9.84701359E-01   # ZH(1,2)
  1  3    -1.00194488E-02   # ZH(1,3)
  2  1     9.84735585E-01   # ZH(2,1)
  2  2    -1.74009567E-01   # ZH(2,2)
  2  3     4.06172803E-03   # ZH(2,3)
  3  1    -5.74306906E-03   # ZH(3,1)
  3  2    -9.15992067E-03   # ZH(3,2)
  3  3     9.99941555E-01   # ZH(3,3)
Block ESIXZMI
  1  1     0.00000000E+00   # Re(ZMI(1,1))
  1  2     1.00000000E+00   # Re(ZMI(1,2))
  2  1     1.00000000E+00   # Re(ZMI(2,1))
  2  2     0.00000000E+00   # Re(ZMI(2,2))
Block NMNMIX
  1  1    -9.87472267E-01   # Re(ZN(1,1))
  1  2     2.87781629E-02   # Re(ZN(1,2))
  1  3    -1.28351094E-01   # Re(ZN(1,3))
  1  4     8.71451789E-02   # Re(ZN(1,4))
  1  5     1.76060918E-04   # Re(ZN(1,5))
  1  6    -1.42200620E-03   # Re(ZN(1,6))
  2  1    -1.40396912E-01   # Re(ZN(2,1))
  2  2    -5.90750461E-01   # Re(ZN(2,2))
  2  3     5.76332856E-01   # Re(ZN(2,3))
  2  4    -5.46917032E-01   # Re(ZN(2,4))
  2  5    -4.68940630E-03   # Re(ZN(2,5))
  2  6     1.67572457E-03   # Re(ZN(2,6))
  3  1     2.79152418E-02   # Re(ZN(3,1))
  3  2    -3.77233793E-02   # Re(ZN(3,2))
  3  3    -7.04178524E-01   # Re(ZN(3,3))
  3  4    -7.08397581E-01   # Re(ZN(3,4))
  3  5    -9.71834794E-03   # Re(ZN(3,5))
  3  6    -2.95191225E-03   # Re(ZN(3,6))
  4  1    -6.63827714E-02   # Re(ZN(4,1))
  4  2     8.05457990E-01   # Re(ZN(4,2))
  4  3     3.94309471E-01   # Re(ZN(4,3))
  4  4    -4.37418131E-01   # Re(ZN(4,4))
  4  5    -3.94379718E-03   # Re(ZN(4,5))
  4  6     7.87132101E-04   # Re(ZN(4,6))
  5  1     3.63204191E-04   # Re(ZN(5,1))
  5  2    -1.70523388E-04   # Re(ZN(5,2))
  5  3     5.58966391E-04   # Re(ZN(5,3))
  5  4    -7.66236383E-03   # Re(ZN(5,4))
  5  5     7.27971861E-01   # Re(ZN(5,5))
  5  6    -6.85563844E-01   # Re(ZN(5,6))
  6  1     1.07866362E-03   # Re(ZN(6,1))
  6  2    -2.31585895E-04   # Re(ZN(6,2))
  6  3     4.33258080E-03   # Re(ZN(6,3))
  6  4     8.18603732E-03   # Re(ZN(6,4))
  6  5    -6.85510721E-01   # Re(ZN(6,5))
  6  6    -7.28002783E-01   # Re(ZN(6,6))
Block ESIXZNI
  1  1    -7.07106781E-01   # Re(ZNI(1,1))
  1  2     0.00000000E+00   # Re(ZNI(1,2))
  1  3    -7.07106781E-01   # Re(ZNI(1,3))
  1  4     0.00000000E+00   # Re(ZNI(1,4))
  2  1     0.00000000E+00   # Re(ZNI(2,1))
  2  2    -7.07106781E-01   # Re(ZNI(2,2))
  2  3     0.00000000E+00   # Re(ZNI(2,3))
  2  4    -7.07106781E-01   # Re(ZNI(2,4))
  3  1     0.00000000E+00   # Re(ZNI(3,1))
  3  2     7.07106781E-01   # Re(ZNI(3,2))
  3  3     0.00000000E+00   # Re(ZNI(3,3))
  3  4    -7.07106781E-01   # Re(ZNI(3,4))
  4  1     7.07106781E-01   # Re(ZNI(4,1))
  4  2     0.00000000E+00   # Re(ZNI(4,2))
  4  3    -7.07106781E-01   # Re(ZNI(4,3))
  4  4     0.00000000E+00   # Re(ZNI(4,4))
Block ZNPMIX
  1  1    -7.07106781E-01   # Re(ZNp(1,1))
  1  2    -7.07106781E-01   # Re(ZNp(1,2))
  2  1     7.07106781E-01   # Re(ZNp(2,1))
  2  2    -7.07106781E-01   # Re(ZNp(2,2))
Block CHARGEMIX
  1  1    -1.73308774E-01   # ZP(1,1)
  1  2     9.84867539E-01   # ZP(1,2)
  2  1     9.84867539E-01   # ZP(2,1)
  2  2     1.73308774E-01   # ZP(2,2)
Block ESIXZPI
  1  1     0.00000000E+00   # Re(ZPI(1,1))
  1  2     1.00000000E+00   # Re(ZPI(1,2))
  2  1     1.00000000E+00   # Re(ZPI(2,1))
  2  2     0.00000000E+00   # Re(ZPI(2,2))
Block ZSSI
  1  1     1.00000000E+00   # ZSSI(1,1)
  1  2     0.00000000E+00   # ZSSI(1,2)
  2  1     0.00000000E+00   # ZSSI(2,1)
  2  2     1.00000000E+00   # ZSSI(2,2)
Block USQMIX
  1  1     0.00000000E+00   # ZU(1,1)
  1  2     0.00000000E+00   # ZU(1,2)
  1  3     1.06992384E-01   # ZU(1,3)
  1  4     0.00000000E+00   # ZU(1,4)
  1  5     9.34079321E-14   # ZU(1,5)
  1  6     9.94259840E-01   # ZU(1,6)
  2  1     0.00000000E+00   # ZU(2,1)
  2  2     0.00000000E+00   # ZU(2,2)
  2  3     9.94259840E-01   # ZU(2,3)
  2  4     0.00000000E+00   # ZU(2,4)
  2  5    -1.00516354E-14   # ZU(2,5)
  2  6    -1.06992384E-01   # ZU(2,6)
  3  1     0.00000000E+00   # ZU(3,1)
  3  2     9.10246310E-03   # ZU(3,2)
  3  3     0.00000000E+00   # ZU(3,3)
  3  4     0.00000000E+00   # ZU(3,4)
  3  5     9.99958572E-01   # ZU(3,5)
  3  6    -9.39433111E-14   # ZU(3,6)
  4  1     1.99217345E-05   # ZU(4,1)
  4  2     0.00000000E+00   # ZU(4,2)
  4  3     0.00000000E+00   # ZU(4,3)
  4  4     1.00000000E+00   # ZU(4,4)
  4  5     0.00000000E+00   # ZU(4,5)
  4  6     0.00000000E+00   # ZU(4,6)
  5  1    -0.00000000E+00   # ZU(5,1)
  5  2    -9.99958572E-01   # ZU(5,2)
  5  3    -0.00000000E+00   # ZU(5,3)
  5  4    -0.00000000E+00   # ZU(5,4)
  5  5     9.10246310E-03   # ZU(5,5)
  5  6    -8.55255328E-16   # ZU(5,6)
  6  1     1.00000000E+00   # ZU(6,1)
  6  2     0.00000000E+00   # ZU(6,2)
  6  3     0.00000000E+00   # ZU(6,3)
  6  4    -1.99217345E-05   # ZU(6,4)
  6  5     0.00000000E+00   # ZU(6,5)
  6  6     0.00000000E+00   # ZU(6,6)
Block SNUMIX
  1  1     0.00000000E+00   # ZV(1,1)
  1  2     0.00000000E+00   # ZV(1,2)
  1  3     1.00000000E+00   # ZV(1,3)
  2  1     0.00000000E+00   # ZV(2,1)
  2  2     1.00000000E+00   # ZV(2,2)
  2  3     0.00000000E+00   # ZV(2,3)
  3  1     1.00000000E+00   # ZV(3,1)
  3  2     0.00000000E+00   # ZV(3,2)
  3  3     0.00000000E+00   # ZV(3,3)
