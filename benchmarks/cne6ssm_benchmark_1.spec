Block SPINFO
     1   FlexibleSUSY
     2   1.0.3
Block MODSEL                 # Select model
#   12   1.000000000e+16                # DRbar parameter output scale (GeV)
Block FlexibleSUSY
    0   1.000000000e-04      # precision goal
    1   0                    # max. iterations (0 = automatic)
    2   0                    # algorithm (0 = two_scale, 1 = lattice)
    3   0                    # calculate SM pole masses
    4   2                    # pole mass loop order
    5   2                    # EWSB loop order
    6   2                    # beta-functions loop order
    7   1                    # threshold corrections (0 = disabled, 1 = enabled)
    8   1                    # Higgs 2-loop corrections O(alpha_t alpha_s)
    9   1                    # Higgs 2-loop corrections O(alpha_b alpha_s)
   10   1                    # Higgs 2-loop corrections O(alpha_t^2 + alpha_t alpha_b + alpha_b^2)
   11   1                    # Higgs 2-loop corrections O(alpha_tau^2)
Block HMIXIN
   31   0.000000000e+00      # mu_phi (pure singlet mass term)
   32   2.000000000e-02      # kappa prime (singlet cubic coupling)
   33   1.000000000e-01      # sigma (singlet-S-Sbar coupling)
Block ESIXRUNIN
    0   1.000000000e+04      # mu prime
   30   0.000000000e+00      # Bmu_phi (soft breaking singlet mass term)
   42   3.000000000e-01      # sigma_L (singlet-L_4-L_4bar coupling)
  101   1.000000000e+04      # B_mu prime
Block ESIXLAMBDAIN
  1  1  5.000000000e-01      # Lambda12(1,1)
  1  2  0.000000000e+00      # Lambda12(1,2)
  2  1  0.000000000e+00      # Lambda12(2,1)
  2  2  5.000000000e-01      # Lambda12(2,2)
Block ESIXKAPPAIN
  1  1  2.000000000e-01      # kappa(1,1)
  1  2  0.000000000e+00      # kappa(1,2)
  1  3  0.000000000e+00      # kappa(1,3)
  2  1  0.000000000e+00      # kappa(2,1)
  2  2  2.000000000e-01      # kappa(2,2)
  2  3  0.000000000e+00      # kappa(2,3)
  3  1  0.000000000e+00      # kappa(3,1)
  3  2  0.000000000e+00      # kappa(3,2)
  3  3  2.000000000e-01      # kappa(3,3)
Block ESIXHEYUKIN
  1  1  0.000000000e+00      # he(1,1)
  1  2  0.000000000e+00      # he(1,2)
  1  3  0.000000000e+00      # he(1,3)
  2  1  0.000000000e+00      # he(2,1)
  2  2  0.000000000e+00      # he(2,2)
  2  3  0.000000000e+00      # he(2,3)
  3  1  0.000000000e+00      # he(3,1)
  3  2  0.000000000e+00      # he(3,2)
  3  3  0.000000000e+00      # he(3,3)
Block ESIXGDYUKIN
  1  1  0.000000000e+00      # gD(1,1)
  1  2  0.000000000e+00      # gD(1,2)
  1  3  0.000000000e+00      # gD(1,3)
  2  1  0.000000000e+00      # gD(2,1)
  2  2  0.000000000e+00      # gD(2,2)
  2  3  0.000000000e+00      # gD(2,3)
  3  1  0.000000000e+00      # gD(3,1)
  3  2  0.000000000e+00      # gD(3,2)
  3  3  0.000000000e+00      # gD(3,3)
Block ESIXFUYUKIN
  1  1  1.000000000e-07      # fu(1,1)
  1  2  0.000000000e+00      # fu(1,2)
  1  3  0.000000000e+00      # fu(1,3)
  2  1  0.000000000e+00      # fu(2,1)
  2  2  1.000000000e-07      # fu(2,2)
  2  3  0.000000000e+00      # fu(2,3)
  3  1  1.000000000e-07      # fu(3,1)
  3  2  0.000000000e+00      # fu(3,2)
  3  3  0.000000000e+00      # fu(3,3)
Block ESIXFDYUKIN
  1  1  1.000000000e-07      # fd(1,1)
  1  2  0.000000000e+00      # fd(1,2)
  1  3  0.000000000e+00      # fd(1,3)
  2  1  0.000000000e+00      # fd(2,1)
  2  2  1.000000000e-07      # fd(2,2)
  2  3  0.000000000e+00      # fd(2,3)
  3  1  0.000000000e+00      # fd(3,1)
  3  2  1.000000000e-07      # fd(3,2)
  3  3  0.000000000e+00      # fd(3,3)
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
     1     2.50000000E+03   # m0
     2     7.50000000E+02   # m12
     3     1.00000000E+01   # TanBeta
     4                  1   # SignLambdax
     5     1.00000000E+03   # Azero
Block EXTPAR
    65     4.00000000E+04   # ssumInput
    72     5.00000000E+00   # QS
Block gauge Q= 2.18243534E+03
     1     3.62989751E-01   # gY
     2     6.33660681E-01   # g2
     3     1.01332692E+00   # g3
     4     4.49611028E-01   # g1p
Block Yu Q= 2.18243534E+03
  1  1     7.25115072E-06   # Yu(1,1)
  1  2     0.00000000E+00   # Yu(1,2)
  1  3     0.00000000E+00   # Yu(1,3)
  2  1     0.00000000E+00   # Yu(2,1)
  2  2     3.31414887E-03   # Yu(2,2)
  2  3     0.00000000E+00   # Yu(2,3)
  3  1     0.00000000E+00   # Yu(3,1)
  3  2     0.00000000E+00   # Yu(3,2)
  3  3     8.75849269E-01   # Yu(3,3)
Block Yd Q= 2.18243534E+03
  1  1     1.37489898E-04   # Yd(1,1)
  1  2     0.00000000E+00   # Yd(1,2)
  1  3     0.00000000E+00   # Yd(1,3)
  2  1     0.00000000E+00   # Yd(2,1)
  2  2     3.01030774E-03   # Yd(2,2)
  2  3     0.00000000E+00   # Yd(2,3)
  3  1     0.00000000E+00   # Yd(3,1)
  3  2     0.00000000E+00   # Yd(3,2)
  3  3     1.34560679E-01   # Yd(3,3)
Block Ye Q= 2.18243534E+03
  1  1     2.76750385E-05   # Ye(1,1)
  1  2     0.00000000E+00   # Ye(1,2)
  1  3     0.00000000E+00   # Ye(1,3)
  2  1     0.00000000E+00   # Ye(2,1)
  2  2     5.72233145E-03   # Ye(2,2)
  2  3     0.00000000E+00   # Ye(2,3)
  3  1     0.00000000E+00   # Ye(3,1)
  3  2     0.00000000E+00   # Ye(3,2)
  3  3     9.86153956E-02   # Ye(3,3)
Block Te Q= 2.18243534E+03
  1  1     1.57246172E-02   # TYe(1,1)
  1  2     0.00000000E+00   # TYe(1,2)
  1  3     0.00000000E+00   # TYe(1,3)
  2  1     0.00000000E+00   # TYe(2,1)
  2  2     3.25126294E+00   # TYe(2,2)
  2  3     0.00000000E+00   # TYe(2,3)
  3  1     0.00000000E+00   # TYe(3,1)
  3  2     0.00000000E+00   # TYe(3,2)
  3  3     5.55430118E+01   # TYe(3,3)
Block Td Q= 2.18243534E+03
  1  1    -9.70486225E-02   # TYd(1,1)
  1  2     0.00000000E+00   # TYd(1,2)
  1  3     0.00000000E+00   # TYd(1,3)
  2  1     0.00000000E+00   # TYd(2,1)
  2  2    -2.12485131E+00   # TYd(2,2)
  2  3     0.00000000E+00   # TYd(2,3)
  3  1     0.00000000E+00   # TYd(3,1)
  3  2     0.00000000E+00   # TYd(3,2)
  3  3    -9.08150456E+01   # TYd(3,3)
Block Tu Q= 2.18243534E+03
  1  1    -4.39653327E-03   # TYu(1,1)
  1  2     0.00000000E+00   # TYu(1,2)
  1  3     0.00000000E+00   # TYu(1,3)
  2  1     0.00000000E+00   # TYu(2,1)
  2  2    -2.00943641E+00   # TYu(2,2)
  2  3     0.00000000E+00   # TYu(2,3)
  3  1     0.00000000E+00   # TYu(3,1)
  3  2     0.00000000E+00   # TYu(3,2)
  3  3    -4.53211911E+02   # TYu(3,3)
Block HMIX Q= 2.18243534E+03
    30     4.56201787E+07   # XiF
    31     0.00000000E+00   # MuPhi
    32     1.69607180E-02   # KappaPr
    33     7.51195097E-02   # Sigmax
    34     6.97544731E+09   # LXiF
   102     2.52120216E+01   # vd
   103     2.40113823E+02   # vu
Block ESIXHEYUK Q= 2.18243534E+03
  1  1     0.00000000E+00   # hE(1,1)
  1  2     0.00000000E+00   # hE(1,2)
  2  1     0.00000000E+00   # hE(2,1)
  2  2     0.00000000E+00   # hE(2,2)
  3  1     0.00000000E+00   # hE(3,1)
  3  2     0.00000000E+00   # hE(3,2)
Block ESIXRUN Q= 2.18243534E+03
    42     4.17474650E-01   # SigmaL
    28     1.32698959E+01   # TKappaPr
    29     4.85137959E+01   # TSigmax
    43     2.11371824E+02   # TSigmaL
    30    -3.99306577E+04   # BMuPhi
    11     2.92140200E+04   # vs
    12     2.73229031E+04   # vsb
    13     2.21920047E+03   # vphi
     1     6.19217105E-02   # Lambdax
     2     3.20942174E+01   # TLambdax
     0     1.47018089E+04   # MuPr
   101    -5.68760177E+06   # BMuPr
Block ESIXGDYUK Q= 2.18243534E+03
  1  1     0.00000000E+00   # gD(1,1)
  1  2     0.00000000E+00   # gD(1,2)
  1  3     0.00000000E+00   # gD(1,3)
  2  1     0.00000000E+00   # gD(2,1)
  2  2     0.00000000E+00   # gD(2,2)
  2  3     0.00000000E+00   # gD(2,3)
  3  1     0.00000000E+00   # gD(3,1)
  3  2     0.00000000E+00   # gD(3,2)
  3  3     0.00000000E+00   # gD(3,3)
Block ESIXFUYUK Q= 2.18243534E+03
  1  1     1.30553662E-07   # fu(1,1)
  1  2     1.07437023E-35   # fu(1,2)
  2  1    -9.42842413E-22   # fu(2,1)
  2  2     1.30553662E-07   # fu(2,2)
  3  1     1.30553662E-07   # fu(3,1)
  3  2    -9.42842413E-22   # fu(3,2)
Block ESIXFDYUK Q= 2.18243534E+03
  1  1     1.63584176E-07   # fd(1,1)
  1  2    -9.78334596E-22   # fd(1,2)
  2  1     1.45608762E-35   # fd(2,1)
  2  2     1.63584176E-07   # fd(2,2)
  3  1    -9.78334596E-22   # fd(3,1)
  3  2     1.63584176E-07   # fd(3,2)
Block ESIXTHETRI Q= 2.18243534E+03
  1  1     0.00000000E+00   # ThE(1,1)
  1  2     0.00000000E+00   # ThE(1,2)
  2  1     0.00000000E+00   # ThE(2,1)
  2  2     0.00000000E+00   # ThE(2,2)
  3  1     0.00000000E+00   # ThE(3,1)
  3  2     0.00000000E+00   # ThE(3,2)
Block ESIXTGDTRI Q= 2.18243534E+03
  1  1     0.00000000E+00   # TgD(1,1)
  1  2     0.00000000E+00   # TgD(1,2)
  1  3     0.00000000E+00   # TgD(1,3)
  2  1     0.00000000E+00   # TgD(2,1)
  2  2     0.00000000E+00   # TgD(2,2)
  2  3     0.00000000E+00   # TgD(2,3)
  3  1     0.00000000E+00   # TgD(3,1)
  3  2     0.00000000E+00   # TgD(3,2)
  3  3     0.00000000E+00   # TgD(3,3)
Block ESIXTFUTRI Q= 2.18243534E+03
  1  1     8.10517212E-05   # Tfu(1,1)
  1  2     3.47739375E-32   # Tfu(1,2)
  2  1    -1.77811582E-18   # Tfu(2,1)
  2  2     8.10517212E-05   # Tfu(2,2)
  3  1     8.10517212E-05   # Tfu(3,1)
  3  2    -1.77811582E-18   # Tfu(3,2)
Block ESIXTFDTRI Q= 2.18243534E+03
  1  1     8.51605285E-05   # Tfd(1,1)
  1  2    -1.77486208E-18   # Tfd(1,2)
  2  1     4.37485934E-32   # Tfd(2,1)
  2  2     8.51605285E-05   # Tfd(2,2)
  3  1    -1.77486208E-18   # Tfd(3,1)
  3  2     8.51605285E-05   # Tfd(3,2)
Block MSQ2 Q= 2.18243534E+03
  1  1     6.19880181E+06   # mq2(1,1)
  1  2     0.00000000E+00   # mq2(1,2)
  1  3     0.00000000E+00   # mq2(1,3)
  2  1     0.00000000E+00   # mq2(2,1)
  2  2     6.19875365E+06   # mq2(2,2)
  2  3     0.00000000E+00   # mq2(2,3)
  3  1     0.00000000E+00   # mq2(3,1)
  3  2     0.00000000E+00   # mq2(3,2)
  3  3     4.35013268E+06   # mq2(3,3)
Block MSE2 Q= 2.18243534E+03
  1  1     6.21898439E+06   # me2(1,1)
  1  2     0.00000000E+00   # me2(1,2)
  1  3     0.00000000E+00   # me2(1,3)
  2  1     0.00000000E+00   # me2(2,1)
  2  2     6.21866487E+06   # me2(2,2)
  2  3     0.00000000E+00   # me2(2,3)
  3  1     0.00000000E+00   # me2(3,1)
  3  2     0.00000000E+00   # me2(3,2)
  3  3     6.12411195E+06   # me2(3,3)
Block MSL2 Q= 2.18243534E+03
  1  1     6.17514603E+06   # ml2(1,1)
  1  2     0.00000000E+00   # ml2(1,2)
  1  3     0.00000000E+00   # ml2(1,3)
  2  1     0.00000000E+00   # ml2(2,1)
  2  2     6.17498745E+06   # ml2(2,2)
  2  3     0.00000000E+00   # ml2(2,3)
  3  1     0.00000000E+00   # ml2(3,1)
  3  2     0.00000000E+00   # ml2(3,2)
  3  3     6.12806454E+06   # ml2(3,3)
Block MSU2 Q= 2.18243534E+03
  1  1     6.26018467E+06   # mu2(1,1)
  1  2     0.00000000E+00   # mu2(1,2)
  1  3     0.00000000E+00   # mu2(1,3)
  2  1     0.00000000E+00   # mu2(2,1)
  2  2     6.26013184E+06   # mu2(2,2)
  2  3     0.00000000E+00   # mu2(2,3)
  3  1     0.00000000E+00   # mu2(3,1)
  3  2     0.00000000E+00   # mu2(3,2)
  3  3     2.59631278E+06   # mu2(3,3)
Block MSD2 Q= 2.18243534E+03
  1  1     6.27351142E+06   # md2(1,1)
  1  2     0.00000000E+00   # md2(1,2)
  1  3     0.00000000E+00   # md2(1,3)
  2  1     0.00000000E+00   # md2(2,1)
  2  2     6.27346708E+06   # md2(2,2)
  2  3     0.00000000E+00   # md2(2,3)
  3  1     0.00000000E+00   # md2(3,1)
  3  2     0.00000000E+00   # md2(3,2)
  3  3     6.18523237E+06   # md2(3,3)
Block MSOFT Q= 2.18243534E+03
    21     5.96288146E+06   # mHd2
    22     4.64293540E+05   # mHu2
    23    -3.89447284E+06   # ms2
    24     6.16530822E+06   # msbar2
    25     4.37594140E+06   # mphi2
    26     5.27631076E+06   # mHp2
    27     5.27653649E+06   # mHpbar2
     1     1.28573023E+02   # MassB
     2     2.26171168E+02   # MassWB
     3     5.50851991E+02   # MassG
     4     1.17903266E+02   # MassBp
Block mX2 Q= 2.18243534E+03
  1  1     5.79265000E+06   # mDx2(1,1)
  1  2     0.00000000E+00   # mDx2(1,2)
  1  3     0.00000000E+00   # mDx2(1,3)
  2  1     0.00000000E+00   # mDx2(2,1)
  2  2     5.79265000E+06   # mDx2(2,2)
  2  3     0.00000000E+00   # mDx2(2,3)
  3  1     0.00000000E+00   # mDx2(3,1)
  3  2     0.00000000E+00   # mDx2(3,2)
  3  3     5.79265000E+06   # mDx2(3,3)
Block mXBar2 Q= 2.18243534E+03
  1  1     5.78039613E+06   # mDxbar2(1,1)
  1  2     0.00000000E+00   # mDxbar2(1,2)
  1  3     0.00000000E+00   # mDxbar2(1,3)
  2  1     0.00000000E+00   # mDxbar2(2,1)
  2  2     5.78039613E+06   # mDxbar2(2,2)
  2  3     0.00000000E+00   # mDxbar2(2,3)
  3  1     0.00000000E+00   # mDxbar2(3,1)
  3  2     0.00000000E+00   # mDxbar2(3,2)
  3  3     5.78039613E+06   # mDxbar2(3,3)
Block ESIXKAPPA Q= 2.18243534E+03
  1  1     4.41036475E-01   # Kappa(1,1)
  1  2     0.00000000E+00   # Kappa(1,2)
  1  3     0.00000000E+00   # Kappa(1,3)
  2  1     0.00000000E+00   # Kappa(2,1)
  2  2     4.41036475E-01   # Kappa(2,2)
  2  3     0.00000000E+00   # Kappa(2,3)
  3  1     0.00000000E+00   # Kappa(3,1)
  3  2     0.00000000E+00   # Kappa(3,2)
  3  3     4.41036475E-01   # Kappa(3,3)
Block ESIXTKAPPA Q= 2.18243534E+03
  1  1    -2.68928911E+02   # TKappa(1,1)
  1  2     0.00000000E+00   # TKappa(1,2)
  1  3     0.00000000E+00   # TKappa(1,3)
  2  1     0.00000000E+00   # TKappa(2,1)
  2  2    -2.68928911E+02   # TKappa(2,2)
  2  3     0.00000000E+00   # TKappa(2,3)
  3  1     0.00000000E+00   # TKappa(3,1)
  3  2     0.00000000E+00   # TKappa(3,2)
  3  3    -2.68928911E+02   # TKappa(3,3)
Block ESIXLAMBDA Q= 2.18243534E+03
  1  1     5.09904930E-01   # Lambda12(1,1)
  1  2     2.12790037E-29   # Lambda12(1,2)
  2  1     2.12790037E-29   # Lambda12(2,1)
  2  2     5.09904930E-01   # Lambda12(2,2)
Block ESIXTLAMBDA Q= 2.18243534E+03
  1  1     1.59095799E+02   # TLambda12(1,1)
  1  2     6.00935009E-26   # TLambda12(1,2)
  2  1     6.00935009E-26   # TLambda12(2,1)
  2  2     1.59095799E+02   # TLambda12(2,2)
Block MASS
   1000021     7.35721859E+02   # Glu
        24     8.04040000E+01   # VWm
   1000091     1.39669926E+04   # ChaP
        31     1.42762666E+04   # VZp
   1000092    -1.39666483E+04   # ChiP(1)
   1000094     1.39666483E+04   # ChiP(2)
   1000024     2.48383955E+02   # Cha(1)
   1000037     1.29318496E+03   # Cha(2)
        37     2.18654262E+03   # Hpm(2)
        92     1.37393230E+04   # SHp0(1)
        94     1.46230617E+04   # SHp0(2)
        91     1.37031839E+04   # SHpp(1)
        93     1.45912585E+04   # SHpp(2)
   1000088     1.05117925E+04   # ChaI(1)
   1000089     1.05117925E+04   # ChaI(2)
   1000012     2.84478076E+03   # Sv(1)
   1000014     2.85327880E+03   # Sv(2)
   1000016     2.85330747E+03   # Sv(3)
        51     8.99487686E+03   # FDX(1)
        52     8.99487686E+03   # FDX(2)
        53     8.99487686E+03   # FDX(3)
        81     1.05316941E+04   # SHIPM(1)
        85     1.05316941E+04   # SHIPM(2)
        83     1.07228823E+04   # SHIPM(3)
        87     1.07228823E+04   # SHIPM(4)
        25     1.21592351E+02   # hh(1)
        35     2.10048382E+03   # hh(2)
        45     2.18530397E+03   # hh(3)
        55     3.14643506E+03   # hh(4)
        65     1.43605651E+04   # hh(5)
  91191138     2.18522597E+03   # Ah(3)
        36     2.54629442E+03   # Ah(4)
  91191137     3.05723352E+03   # Ah(5)
   1000001     2.31925003E+03   # Sd(1)
   1000003     2.70686541E+03   # Sd(2)
   1000005     2.70687495E+03   # Sd(3)
   2000001     2.87535607E+03   # Sd(4)
   2000003     2.89176599E+03   # Sd(5)
   2000005     2.89177414E+03   # Sd(6)
   1000011     2.66189561E+03   # Se(1)
   1000013     2.68012170E+03   # Se(2)
   1000015     2.68018310E+03   # Se(3)
   2000011     2.84629852E+03   # Se(4)
   2000013     2.85471888E+03   # Se(5)
   2000015     2.85474729E+03   # Se(6)
   1000002     1.89477242E+03   # Su(1)
   1000004     2.32440349E+03   # Su(2)
   1000006     2.70583126E+03   # Su(3)
   2000002     2.70584129E+03   # Su(4)
   2000004     2.71634355E+03   # Su(5)
   2000006     2.71635307E+03   # Su(6)
   1000051     8.82645954E+03   # SDX(1)
   2000051     8.82645954E+03   # SDX(2)
   1000052     8.82645954E+03   # SDX(3)
   2000052     9.51236659E+03   # SDX(4)
   1000053     9.51236659E+03   # SDX(5)
   2000053     9.51236659E+03   # SDX(6)
   1000081    -4.07250364E-14   # ChiI(1)
   1000082     1.11262868E-13   # ChiI(2)
   1000083     1.51987906E-13   # ChiI(3)
   1000084    -1.05114472E+04   # ChiI(4)
   1000085     1.05114472E+04   # ChiI(5)
   1000086     1.05114472E+04   # ChiI(6)
   1000087    -1.05114472E+04   # ChiI(7)
        82     3.44887516E+03   # SHI0(1)
        86     3.44887516E+03   # SHI0(2)
        84     3.44887516E+03   # SHI0(3)
        88     1.05629322E+04   # SHI0(4)
   9994453     1.05629322E+04   # SHI0(5)
   9994454     1.07517001E+04   # SHI0(6)
   9994455     1.07517001E+04   # SHI0(7)
   1000022     1.30760376E+02   # Chi(1)
   1000023     2.48234981E+02   # Chi(2)
   1000025    -1.28986140E+03   # Chi(3)
   1000035     1.29226737E+03   # Chi(4)
   1000045     2.11953558E+03   # Chi(5)
   1000055    -2.19070404E+03   # Chi(6)
   1000065    -1.41506098E+04   # Chi(7)
   1000075     1.43942974E+04   # Chi(8)
Block UHNIMIX
  1  1    -2.93715088E-10   # UHI0(1,1)
  1  2    -9.81736028E-11   # UHI0(1,2)
  1  3    -3.21278927E-10   # UHI0(1,3)
  1  4    -1.07386899E-10   # UHI0(1,4)
  1  5    -9.48364480E-01   # UHI0(1,5)
  1  6     1.93452737E-04   # UHI0(1,6)
  1  7    -3.17182560E-01   # UHI0(1,7)
  2  1     0.00000000E+00   # UHI0(2,1)
  2  2     3.09895804E-10   # UHI0(2,2)
  2  3    -5.16987883E-26   # UHI0(2,3)
  2  4     3.38978131E-10   # UHI0(2,4)
  2  5    -2.13162374E-16   # UHI0(2,5)
  2  6     9.99999814E-01   # UHI0(2,6)
  2  7     6.09909641E-04   # UHI0(2,7)
  3  1    -9.82336672E-11   # UHI0(3,1)
  3  2     2.93535938E-10   # UHI0(3,2)
  3  3    -1.07452455E-10   # UHI0(3,3)
  3  4     3.21082916E-10   # UHI0(3,4)
  3  5    -3.17182619E-01   # UHI0(3,5)
  3  6    -5.78416640E-04   # UHI0(3,6)
  3  7     9.48364303E-01   # UHI0(3,7)
  4  1    -7.82655750E-01   # UHI0(4,1)
  4  2    -2.35628436E-16   # UHI0(4,2)
  4  3    -6.22454799E-01   # UHI0(4,3)
  4  4     1.47301391E-20   # UHI0(4,4)
  4  5     4.53263931E-10   # UHI0(4,5)
  4  6     1.01514935E-25   # UHI0(4,6)
  4  7     1.24577334E-23   # UHI0(4,7)
  5  1    -5.66720316E-18   # UHI0(5,1)
  5  2     7.82655750E-01   # UHI0(5,2)
  5  3    -9.39327635E-17   # UHI0(5,3)
  5  4     6.22454799E-01   # UHI0(5,4)
  5  5    -1.26807316E-17   # UHI0(5,5)
  5  6    -4.53263931E-10   # UHI0(5,6)
  5  7    -4.53263931E-10   # UHI0(5,7)
  6  1    -6.22454799E-01   # UHI0(6,1)
  6  2     2.84639077E-16   # UHI0(6,2)
  6  3     7.82655750E-01   # UHI0(6,3)
  6  4    -1.85212293E-20   # UHI0(6,4)
  6  5    -7.23629316E-11   # UHI0(6,5)
  6  6    -1.66501063E-26   # UHI0(6,6)
  6  7    -1.78383208E-23   # UHI0(6,7)
  7  1    -4.50718953E-18   # UHI0(7,1)
  7  2     6.22454799E-01   # UHI0(7,2)
  7  3    -7.30534638E-17   # UHI0(7,3)
  7  4    -7.82655750E-01   # UHI0(7,4)
  7  5    -1.23328760E-17   # UHI0(7,5)
  7  6     7.23629316E-11   # UHI0(7,6)
  7  7     7.23629316E-11   # UHI0(7,7)
Block UHNPMIX
  1  1    -6.50872725E-01   # UHp0(1,1)
  1  2     7.59186865E-01   # UHp0(1,2)
  2  1     7.59186865E-01   # UHp0(2,1)
  2  2     6.50872725E-01   # UHp0(2,2)
Block UHPPMIX
  1  1     6.50656854E-01   # UHpp(1,1)
  1  2     7.59371884E-01   # UHpp(1,2)
  2  1     7.59371884E-01   # UHpp(2,1)
  2  2    -6.50656854E-01   # UHpp(2,2)
Block UMIX
  1  1     9.95907401E-01   # Re(UM(1,1))
  1  2    -9.03794741E-02   # Re(UM(1,2))
  2  1     9.03794741E-02   # Re(UM(2,1))
  2  2     9.95907401E-01   # Re(UM(2,2))
Block VMIX
  1  1     9.99658271E-01   # Re(UP(1,1))
  1  2    -2.61408125E-02   # Re(UP(1,2))
  2  1     2.61408125E-02   # Re(UP(2,1))
  2  2     9.99658271E-01   # Re(UP(2,2))
Block NMAMIX
  1  1    -1.04466080E-01   # ZA(1,1)
  1  2     9.94525677E-01   # ZA(1,2)
  1  3     1.71580255E-03   # ZA(1,3)
  1  4    -1.60368423E-03   # ZA(1,4)
  1  5    -3.23840351E-09   # ZA(1,5)
  2  1     3.78220194E-04   # ZA(2,1)
  2  2     2.40121926E-03   # ZA(2,2)
  2  3    -7.30347822E-01   # ZA(2,3)
  2  4     6.83071116E-01   # ZA(2,4)
  2  5     3.19599553E-07   # ZA(2,5)
  3  1    -9.94518574E-01   # ZA(3,1)
  3  2    -1.04463852E-01   # ZA(3,2)
  3  3    -7.30008060E-04   # ZA(3,3)
  3  4     1.37359654E-04   # ZA(3,4)
  3  5     4.42233326E-03   # ZA(3,5)
  4  1    -2.52197618E-03   # ZA(4,1)
  4  2    -2.65579452E-04   # ZA(4,2)
  4  3     5.93445118E-01   # ZA(4,3)
  4  4     6.34521193E-01   # ZA(4,4)
  4  5    -4.95176046E-01   # ZA(4,5)
  5  1    -3.62492787E-03   # ZA(5,1)
  5  2    -3.80380886E-04   # ZA(5,2)
  5  3    -3.38247651E-01   # ZA(5,3)
  5  4    -3.61654691E-01   # ZA(5,4)
  5  5    -8.68781403E-01   # ZA(5,5)
Block DSQMIX
  1  1    -0.00000000E+00   # ZD(1,1)
  1  2    -0.00000000E+00   # ZD(1,2)
  1  3    -9.99941933E-01   # ZD(1,3)
  1  4    -0.00000000E+00   # ZD(1,4)
  1  5     1.34525224E-12   # ZD(1,5)
  1  6    -1.07763685E-02   # ZD(1,6)
  2  1     0.00000000E+00   # ZD(2,1)
  2  2    -9.99999773E-01   # ZD(2,2)
  2  3    -9.06557339E-16   # ZD(2,3)
  2  4     0.00000000E+00   # ZD(2,4)
  2  5    -6.73835830E-04   # ZD(2,5)
  2  6     0.00000000E+00   # ZD(2,6)
  3  1    -1.00000000E+00   # ZD(3,1)
  3  2    -0.00000000E+00   # ZD(3,2)
  3  3    -0.00000000E+00   # ZD(3,3)
  3  4    -3.07762523E-05   # ZD(3,4)
  3  5    -0.00000000E+00   # ZD(3,5)
  3  6    -0.00000000E+00   # ZD(3,6)
  4  1     0.00000000E+00   # ZD(4,1)
  4  2     0.00000000E+00   # ZD(4,2)
  4  3     1.07763685E-02   # ZD(4,3)
  4  4     0.00000000E+00   # ZD(4,4)
  4  5    -1.44985477E-14   # ZD(4,5)
  4  6    -9.99941933E-01   # ZD(4,6)
  5  1    -0.00000000E+00   # ZD(5,1)
  5  2    -6.73835830E-04   # ZD(5,2)
  5  3     1.34536796E-12   # ZD(5,3)
  5  4    -0.00000000E+00   # ZD(5,4)
  5  5     9.99999773E-01   # ZD(5,5)
  5  6    -0.00000000E+00   # ZD(5,6)
  6  1     3.07762523E-05   # ZD(6,1)
  6  2     0.00000000E+00   # ZD(6,2)
  6  3     0.00000000E+00   # ZD(6,3)
  6  4    -1.00000000E+00   # ZD(6,4)
  6  5     0.00000000E+00   # ZD(6,5)
  6  6     0.00000000E+00   # ZD(6,6)
Block ESIXZDX
  1  1     0.00000000E+00   # ZDX(1,1)
  1  2     0.00000000E+00   # ZDX(1,2)
  1  3     6.79401136E-01   # ZDX(1,3)
  1  4     0.00000000E+00   # ZDX(1,4)
  1  5     0.00000000E+00   # ZDX(1,5)
  1  6     7.33767058E-01   # ZDX(1,6)
  2  1     6.79401136E-01   # ZDX(2,1)
  2  2     0.00000000E+00   # ZDX(2,2)
  2  3     0.00000000E+00   # ZDX(2,3)
  2  4     7.33767058E-01   # ZDX(2,4)
  2  5     0.00000000E+00   # ZDX(2,5)
  2  6     0.00000000E+00   # ZDX(2,6)
  3  1    -0.00000000E+00   # ZDX(3,1)
  3  2    -6.79401136E-01   # ZDX(3,2)
  3  3    -0.00000000E+00   # ZDX(3,3)
  3  4    -0.00000000E+00   # ZDX(3,4)
  3  5    -7.33767058E-01   # ZDX(3,5)
  3  6    -0.00000000E+00   # ZDX(3,6)
  4  1     7.33767058E-01   # ZDX(4,1)
  4  2     0.00000000E+00   # ZDX(4,2)
  4  3     0.00000000E+00   # ZDX(4,3)
  4  4    -6.79401136E-01   # ZDX(4,4)
  4  5     0.00000000E+00   # ZDX(4,5)
  4  6     0.00000000E+00   # ZDX(4,6)
  5  1     0.00000000E+00   # ZDX(5,1)
  5  2     0.00000000E+00   # ZDX(5,2)
  5  3     7.33767058E-01   # ZDX(5,3)
  5  4     0.00000000E+00   # ZDX(5,4)
  5  5     0.00000000E+00   # ZDX(5,5)
  5  6    -6.79401136E-01   # ZDX(5,6)
  6  1     0.00000000E+00   # ZDX(6,1)
  6  2    -7.33767058E-01   # ZDX(6,2)
  6  3     0.00000000E+00   # ZDX(6,3)
  6  4     0.00000000E+00   # ZDX(6,4)
  6  5     6.79401136E-01   # ZDX(6,5)
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
  1  3     2.06262607E-02   # ZE(1,3)
  1  4     0.00000000E+00   # ZE(1,4)
  1  5     0.00000000E+00   # ZE(1,5)
  1  6     9.99787256E-01   # ZE(1,6)
  2  1     0.00000000E+00   # ZE(2,1)
  2  2     1.25861629E-03   # ZE(2,2)
  2  3     0.00000000E+00   # ZE(2,3)
  2  4     0.00000000E+00   # ZE(2,4)
  2  5     9.99999208E-01   # ZE(2,5)
  2  6     0.00000000E+00   # ZE(2,6)
  3  1     6.08813769E-06   # ZE(3,1)
  3  2     0.00000000E+00   # ZE(3,2)
  3  3     0.00000000E+00   # ZE(3,3)
  3  4     1.00000000E+00   # ZE(3,4)
  3  5     0.00000000E+00   # ZE(3,5)
  3  6     0.00000000E+00   # ZE(3,6)
  4  1     0.00000000E+00   # ZE(4,1)
  4  2     0.00000000E+00   # ZE(4,2)
  4  3     9.99787256E-01   # ZE(4,3)
  4  4     0.00000000E+00   # ZE(4,4)
  4  5     0.00000000E+00   # ZE(4,5)
  4  6    -2.06262607E-02   # ZE(4,6)
  5  1     0.00000000E+00   # ZE(5,1)
  5  2     9.99999208E-01   # ZE(5,2)
  5  3     0.00000000E+00   # ZE(5,3)
  5  4     0.00000000E+00   # ZE(5,4)
  5  5    -1.25861629E-03   # ZE(5,5)
  5  6     0.00000000E+00   # ZE(5,6)
  6  1     1.00000000E+00   # ZE(6,1)
  6  2     0.00000000E+00   # ZE(6,2)
  6  3     0.00000000E+00   # ZE(6,3)
  6  4    -6.08813769E-06   # ZE(6,4)
  6  5     0.00000000E+00   # ZE(6,5)
  6  6     0.00000000E+00   # ZE(6,6)
Block NMHMIX
  1  1     1.04954826E-01   # ZH(1,1)
  1  2     9.94465377E-01   # ZH(1,2)
  1  3    -1.24528260E-03   # ZH(1,3)
  1  4    -4.57917477E-03   # ZH(1,4)
  1  5    -7.61467455E-04   # ZH(1,5)
  2  1     2.91634163E-04   # ZH(2,1)
  2  2     4.19407977E-03   # ZH(2,2)
  2  3     6.92444196E-01   # ZH(2,3)
  2  4     7.00512341E-01   # ZH(2,4)
  2  5     1.72585691E-01   # ZH(2,5)
  3  1    -9.94471856E-01   # ZH(3,1)
  3  2     1.04955362E-01   # ZH(3,2)
  3  3    -6.00622480E-04   # ZH(3,3)
  3  4    -3.83669579E-04   # ZH(3,4)
  3  5     3.09697535E-03   # ZH(3,5)
  4  1    -3.15693321E-03   # ZH(4,1)
  4  2     2.95473153E-04   # ZH(4,2)
  4  3     1.21511553E-01   # ZH(4,3)
  4  4     1.22559971E-01   # ZH(4,4)
  4  5    -9.84989311E-01   # ZH(4,5)
  5  1     4.00667506E-04   # ZH(5,1)
  5  2     2.30416738E-03   # ZH(5,2)
  5  3    -7.11163881E-01   # ZH(5,3)
  5  4     7.03022331E-01   # ZH(5,4)
  5  5    -2.56668518E-04   # ZH(5,5)
Block ESIXZMI
  1  1     0.00000000E+00   # Re(ZMI(1,1))
  1  2     1.00000000E+00   # Re(ZMI(1,2))
  2  1     1.00000000E+00   # Re(ZMI(2,1))
  2  2     0.00000000E+00   # Re(ZMI(2,2))
Block NMNMIX
  1  1     9.99311514E-01   # Re(ZN(1,1))
  1  2    -7.13310771E-03   # Re(ZN(1,2))
  1  3     3.56511510E-02   # Re(ZN(1,3))
  1  4    -7.30701881E-03   # Re(ZN(1,4))
  1  5     1.55693105E-04   # Re(ZN(1,5))
  1  6     3.51518429E-05   # Re(ZN(1,6))
  1  7    -3.86740600E-04   # Re(ZN(1,7))
  1  8     1.02202475E-03   # Re(ZN(1,8))
  2  1     9.52811159E-03   # Re(ZN(2,1))
  2  2     9.97756081E-01   # Re(ZN(2,2))
  2  3    -6.36771855E-02   # Re(ZN(2,3))
  2  4     1.83626445E-02   # Re(ZN(2,4))
  2  5     2.62359583E-06   # Re(ZN(2,5))
  2  6    -2.74658825E-05   # Re(ZN(2,6))
  2  7     2.12316069E-04   # Re(ZN(2,7))
  2  8    -2.56498998E-05   # Re(ZN(2,8))
  3  1    -1.97815643E-02   # Re(ZN(3,1))
  3  2     3.22200746E-02   # Re(ZN(3,2))
  3  3     7.05855854E-01   # Re(ZN(3,3))
  3  4     7.07327111E-01   # Re(ZN(3,4))
  3  5    -3.10587656E-04   # Re(ZN(3,5))
  3  6    -3.16317039E-03   # Re(ZN(3,6))
  3  7    -4.03292057E-03   # Re(ZN(3,7))
  3  8     2.47519023E-04   # Re(ZN(3,8))
  4  1    -2.98884006E-02   # Re(ZN(4,1))
  4  2     5.82561031E-02   # Re(ZN(4,2))
  4  3     7.04565925E-01   # Re(ZN(4,3))
  4  4    -7.06598757E-01   # Re(ZN(4,4))
  4  5     3.28017469E-04   # Re(ZN(4,5))
  4  6     2.42323320E-03   # Re(ZN(4,6))
  4  7    -3.45726865E-03   # Re(ZN(4,7))
  4  8     1.76107241E-04   # Re(ZN(4,8))
  5  1    -2.30978236E-04   # Re(ZN(5,1))
  5  2    -9.50883978E-05   # Re(ZN(5,2))
  5  3    -3.57734891E-03   # Re(ZN(5,3))
  5  4     1.90017897E-03   # Re(ZN(5,4))
  5  5     4.79702442E-01   # Re(ZN(5,5))
  5  6     4.99628841E-01   # Re(ZN(5,6))
  5  7    -7.21276639E-01   # Re(ZN(5,7))
  5  8     3.58100641E-04   # Re(ZN(5,8))
  6  1     5.01969890E-05   # Re(ZN(6,1))
  6  2     6.95386662E-05   # Re(ZN(6,2))
  6  3     3.94095307E-03   # Re(ZN(6,3))
  6  4     2.56074807E-03   # Re(ZN(6,4))
  6  5     4.99493556E-01   # Re(ZN(6,5))
  6  6     5.20338713E-01   # Re(ZN(6,6))
  6  7     6.92626592E-01   # Re(ZN(6,7))
  6  8     3.46151490E-04   # Re(ZN(6,8))
  7  1     6.49494371E-04   # Re(ZN(7,1))
  7  2    -1.00938234E-05   # Re(ZN(7,2))
  7  3    -2.62228142E-05   # Re(ZN(7,3))
  7  4    -1.67243512E-03   # Re(ZN(7,4))
  7  5     5.10358355E-01   # Re(ZN(7,5))
  7  6    -4.89461381E-01   # Re(ZN(7,6))
  7  7     2.03649677E-05   # Re(ZN(7,7))
  7  8    -7.07077567E-01   # Re(ZN(7,8))
  8  1     7.80061209E-04   # Re(ZN(8,1))
  8  2    -1.06359000E-05   # Re(ZN(8,2))
  8  3     5.02713424E-04   # Re(ZN(8,3))
  8  4     1.73490068E-03   # Re(ZN(8,4))
  8  5    -5.09829261E-01   # Re(ZN(8,5))
  8  6     4.89928895E-01   # Re(ZN(8,6))
  8  7    -4.94153024E-05   # Re(ZN(8,7))
  8  8    -7.07135015E-01   # Re(ZN(8,8))
Block ZNIMIX
  1  1     8.99882964E-11   # Re(ZNI(1,1))
  1  2    -1.55864286E-10   # Re(ZNI(1,2))
  1  3    -1.18383031E-09   # Re(ZNI(1,3))
  1  4     6.83484745E-10   # Re(ZNI(1,4))
  1  5     3.25057582E-01   # Re(ZNI(1,5))
  1  6     3.25057583E-01   # Re(ZNI(1,6))
  1  7    -8.88073835E-01   # Re(ZNI(1,7))
  2  1    -1.95754039E-10   # Re(ZNI(2,1))
  2  2     1.95754002E-10   # Re(ZNI(2,2))
  2  3    -1.48680333E-09   # Re(ZNI(2,3))
  2  4     1.48680334E-09   # Re(ZNI(2,4))
  2  5    -7.07106781E-01   # Re(ZNI(2,5))
  2  6     7.07106782E-01   # Re(ZNI(2,6))
  2  7     5.35110235E-10   # Re(ZNI(2,7))
  3  1    -1.73844040E-10   # Re(ZNI(3,1))
  3  2    -3.01106741E-10   # Re(ZNI(3,2))
  3  3    -2.28698454E-09   # Re(ZNI(3,3))
  3  4    -1.32039114E-09   # Re(ZNI(3,4))
  3  5    -6.27963031E-01   # Re(ZNI(3,5))
  3  6    -6.27963030E-01   # Re(ZNI(3,6))
  3  7    -4.59700842E-01   # Re(ZNI(3,7))
  4  1    -7.07106781E-01   # Re(ZNI(4,1))
  4  2    -3.39934538E-21   # Re(ZNI(4,2))
  4  3    -7.07106781E-01   # Re(ZNI(4,3))
  4  4     4.35072305E-21   # Re(ZNI(4,4))
  4  5     1.68255737E-09   # Re(ZNI(4,5))
  4  6    -1.01489952E-23   # Re(ZNI(4,6))
  4  7     1.48680334E-09   # Re(ZNI(4,7))
  5  1    -7.07106781E-01   # Re(ZNI(5,1))
  5  2     2.55155602E-06   # Re(ZNI(5,2))
  5  3     7.07106781E-01   # Re(ZNI(5,3))
  5  4    -2.55155602E-06   # Re(ZNI(5,4))
  5  5    -1.29104930E-09   # Re(ZNI(5,5))
  5  6     4.65868055E-15   # Re(ZNI(5,6))
  5  7    -1.48680404E-09   # Re(ZNI(5,7))
  6  1    -2.55155602E-06   # Re(ZNI(6,1))
  6  2    -7.07106781E-01   # Re(ZNI(6,2))
  6  3     2.55155602E-06   # Re(ZNI(6,3))
  6  4     7.07106781E-01   # Re(ZNI(6,4))
  6  5    -4.70068096E-15   # Re(ZNI(6,5))
  6  6    -1.29104930E-09   # Re(ZNI(6,6))
  6  7     1.95748674E-10   # Re(ZNI(6,7))
  7  1     2.96461532E-21   # Re(ZNI(7,1))
  7  2    -7.07106781E-01   # Re(ZNI(7,2))
  7  3     8.47032947E-21   # Re(ZNI(7,3))
  7  4    -7.07106781E-01   # Re(ZNI(7,4))
  7  5    -4.20004918E-17   # Re(ZNI(7,5))
  7  6     1.68255737E-09   # Re(ZNI(7,6))
  7  7     1.95754038E-10   # Re(ZNI(7,7))
Block ZNPMIX
  1  1    -7.07106781E-01   # Re(ZNp(1,1))
  1  2    -7.07106781E-01   # Re(ZNp(1,2))
  2  1     7.07106781E-01   # Re(ZNp(2,1))
  2  2    -7.07106781E-01   # Re(ZNp(2,2))
Block CHARGEMIX
  1  1    -1.04631720E-01   # ZP(1,1)
  1  2     9.94511037E-01   # ZP(1,2)
  2  1     9.94511037E-01   # ZP(2,1)
  2  2     1.04631720E-01   # ZP(2,2)
Block ESIXZPI
  1  1     0.00000000E+00   # Re(ZPI(1,1))
  1  2     1.00000000E+00   # Re(ZPI(1,2))
  2  1     1.00000000E+00   # Re(ZPI(2,1))
  2  2     0.00000000E+00   # Re(ZPI(2,2))
Block USQMIX
  1  1     0.00000000E+00   # ZU(1,1)
  1  2     0.00000000E+00   # ZU(1,2)
  1  3     5.78747159E-02   # ZU(1,3)
  1  4     0.00000000E+00   # ZU(1,4)
  1  5     0.00000000E+00   # ZU(1,5)
  1  6     9.98323854E-01   # ZU(1,6)
  2  1     0.00000000E+00   # ZU(2,1)
  2  2     0.00000000E+00   # ZU(2,2)
  2  3     9.98323854E-01   # ZU(2,3)
  2  4     0.00000000E+00   # ZU(2,4)
  2  5     0.00000000E+00   # ZU(2,5)
  2  6    -5.78747159E-02   # ZU(2,6)
  3  1    -0.00000000E+00   # ZU(3,1)
  3  2     9.99986179E-01   # ZU(3,2)
  3  3    -0.00000000E+00   # ZU(3,3)
  3  4    -0.00000000E+00   # ZU(3,4)
  3  5     5.25752324E-03   # ZU(3,5)
  3  6    -0.00000000E+00   # ZU(3,6)
  4  1    -1.00000000E+00   # ZU(4,1)
  4  2    -0.00000000E+00   # ZU(4,2)
  4  3    -0.00000000E+00   # ZU(4,3)
  4  4    -1.15030055E-05   # ZU(4,4)
  4  5    -0.00000000E+00   # ZU(4,5)
  4  6    -0.00000000E+00   # ZU(4,6)
  5  1     0.00000000E+00   # ZU(5,1)
  5  2    -5.25752324E-03   # ZU(5,2)
  5  3     0.00000000E+00   # ZU(5,3)
  5  4     0.00000000E+00   # ZU(5,4)
  5  5     9.99986179E-01   # ZU(5,5)
  5  6     0.00000000E+00   # ZU(5,6)
  6  1     1.15030055E-05   # ZU(6,1)
  6  2     0.00000000E+00   # ZU(6,2)
  6  3     0.00000000E+00   # ZU(6,3)
  6  4    -1.00000000E+00   # ZU(6,4)
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
