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
     1     1.25000000E+02   # m0
     2     5.00000000E+02   # m12
     3     1.00000000E+01   # TanBeta
     4                  1   # SignMu
     5     0.00000000E+00   # Azero
Block gauge Q= 8.76740936E+02
     1     3.62389656E-01   # gY
     2     6.43201673E-01   # g2
     3     1.06219234E+00   # g3
Block Yu Q= 8.76740936E+02
  1  1     7.32064958E-06   # Yu(1,1)
  1  2     0.00000000E+00   # Yu(1,2)
  1  3     0.00000000E+00   # Yu(1,3)
  2  1     0.00000000E+00   # Yu(2,1)
  2  2     3.34591256E-03   # Yu(2,2)
  2  3     0.00000000E+00   # Yu(2,3)
  3  1     0.00000000E+00   # Yu(3,1)
  3  2     0.00000000E+00   # Yu(3,2)
  3  3     8.60708818E-01   # Yu(3,3)
Block Yd Q= 8.76740936E+02
  1  1     1.40989774E-04   # Yd(1,1)
  1  2     0.00000000E+00   # Yd(1,2)
  1  3     0.00000000E+00   # Yd(1,3)
  2  1     0.00000000E+00   # Yd(2,1)
  2  2     3.08693594E-03   # Yd(2,2)
  2  3     0.00000000E+00   # Yd(2,3)
  3  1     0.00000000E+00   # Yd(3,1)
  3  2     0.00000000E+00   # Yd(3,2)
  3  3     1.33150195E-01   # Yd(3,3)
Block Ye Q= 8.76740936E+02
  1  1     2.79523874E-05   # Ye(1,1)
  1  2     0.00000000E+00   # Ye(1,2)
  1  3     0.00000000E+00   # Ye(1,3)
  2  1     0.00000000E+00   # Ye(2,1)
  2  2     5.77967521E-03   # Ye(2,2)
  2  3     0.00000000E+00   # Ye(2,3)
  3  1     0.00000000E+00   # Ye(3,1)
  3  2     0.00000000E+00   # Ye(3,2)
  3  3     1.00559872E-01   # Ye(3,3)
Block Te Q= 8.76740936E+02
  1  1    -8.38586790E-03   # TYe(1,1)
  1  2     0.00000000E+00   # TYe(1,2)
  1  3     0.00000000E+00   # TYe(1,3)
  2  1     0.00000000E+00   # TYe(2,1)
  2  2    -1.73390259E+00   # TYe(2,2)
  2  3     0.00000000E+00   # TYe(2,3)
  3  1     0.00000000E+00   # TYe(3,1)
  3  2     0.00000000E+00   # TYe(3,2)
  3  3    -3.00034832E+01   # TYe(3,3)
Block Td Q= 8.76740936E+02
  1  1    -1.97422972E-01   # TYd(1,1)
  1  2     0.00000000E+00   # TYd(1,2)
  1  3     0.00000000E+00   # TYd(1,3)
  2  1     0.00000000E+00   # TYd(2,1)
  2  2    -4.32251217E+00   # TYd(2,2)
  2  3     0.00000000E+00   # TYd(2,3)
  3  1     0.00000000E+00   # TYd(3,1)
  3  2     0.00000000E+00   # TYd(3,2)
  3  3    -1.74273641E+02   # TYd(3,3)
Block Tu Q= 8.76740936E+02
  1  1    -8.38049066E-03   # TYu(1,1)
  1  2     0.00000000E+00   # TYu(1,2)
  1  3     0.00000000E+00   # TYu(1,3)
  2  1     0.00000000E+00   # TYu(2,1)
  2  2    -3.83029735E+00   # TYu(2,2)
  2  3     0.00000000E+00   # TYu(2,3)
  3  1     0.00000000E+00   # TYu(3,1)
  3  2     0.00000000E+00   # TYu(3,2)
  3  3    -7.60783087E+02   # TYu(3,3)
Block MSQ2 Q= 8.76740936E+02
  1  1     1.04148898E+06   # mq2(1,1)
  1  2     0.00000000E+00   # mq2(1,2)
  1  3     0.00000000E+00   # mq2(1,3)
  2  1     0.00000000E+00   # mq2(2,1)
  2  2     1.04148367E+06   # mq2(2,2)
  2  3     0.00000000E+00   # mq2(2,3)
  3  1     0.00000000E+00   # mq2(3,1)
  3  2     0.00000000E+00   # mq2(3,2)
  3  3     8.85030976E+05   # mq2(3,3)
Block MSE2 Q= 8.76740936E+02
  1  1     4.92998609E+04   # me2(1,1)
  1  2     0.00000000E+00   # me2(1,2)
  1  3     0.00000000E+00   # me2(1,3)
  2  1     0.00000000E+00   # me2(2,1)
  2  2     4.92950442E+04   # me2(2,2)
  2  3     0.00000000E+00   # me2(2,3)
  3  1     0.00000000E+00   # me2(3,1)
  3  2     0.00000000E+00   # me2(3,2)
  3  3     4.78436592E+04   # me2(3,3)
Block MSL2 Q= 8.76740936E+02
  1  1     1.25610860E+05   # ml2(1,1)
  1  2     0.00000000E+00   # ml2(1,2)
  1  3     0.00000000E+00   # ml2(1,3)
  2  1     0.00000000E+00   # ml2(2,1)
  2  2     1.25608497E+05   # ml2(2,2)
  2  3     0.00000000E+00   # ml2(2,3)
  3  1     0.00000000E+00   # ml2(3,1)
  3  2     0.00000000E+00   # ml2(3,2)
  3  3     1.24896743E+05   # ml2(3,3)
Block MSU2 Q= 8.76740936E+02
  1  1     9.65435806E+05   # mu2(1,1)
  1  2     0.00000000E+00   # mu2(1,2)
  1  3     0.00000000E+00   # mu2(1,3)
  2  1     0.00000000E+00   # mu2(2,1)
  2  2     9.65430378E+05   # mu2(2,2)
  2  3     0.00000000E+00   # mu2(2,3)
  3  1     0.00000000E+00   # mu2(3,1)
  3  2     0.00000000E+00   # mu2(3,2)
  3  3     6.54686474E+05   # mu2(3,3)
Block MSD2 Q= 8.76740936E+02
  1  1     9.56443691E+05   # md2(1,1)
  1  2     0.00000000E+00   # md2(1,2)
  1  3     0.00000000E+00   # md2(1,3)
  2  1     0.00000000E+00   # md2(2,1)
  2  2     9.56438360E+05   # md2(2,2)
  2  3     0.00000000E+00   # md2(2,3)
  3  1     0.00000000E+00   # md2(3,1)
  3  2     0.00000000E+00   # md2(3,2)
  3  3     9.46966332E+05   # md2(3,3)
Block MASS
   1000021     1.14926500E+03   # Glu
        24     8.04040000E+01   # VWm
   1000024     3.85827419E+02   # Cha(1)
   1000037     6.50628043E+02   # Cha(2)
        25     1.14886245E+02   # hh(1)
        35     7.19604829E+02   # hh(2)
        37     7.24070143E+02   # Hpm(2)
        36     7.19332637E+02   # Ah(2)
   1000012     3.51853616E+02   # Sv(1)
   1000014     3.53021627E+02   # Sv(2)
   1000016     3.53025498E+02   # Sv(3)
   1000022     2.03950341E+02   # Chi(1)
   1000023     3.85813554E+02   # Chi(2)
   1000025    -6.36719046E+02   # Chi(3)
   1000035     6.50294202E+02   # Chi(4)
   1000001     9.68501193E+02   # Sd(1)
   1000003     1.00994947E+03   # Sd(2)
   1000005     1.01314860E+03   # Sd(3)
   2000001     1.01315244E+03   # Sd(4)
   2000003     1.05768179E+03   # Sd(5)
   2000005     1.05768367E+03   # Sd(6)
   1000011     2.22729550E+02   # Se(1)
   1000013     2.29867298E+02   # Se(2)
   1000015     2.29890985E+02   # Se(3)
   2000011     3.61924087E+02   # Se(4)
   2000013     3.61928102E+02   # Se(5)
   2000015     3.63067985E+02   # Se(6)
   1000002     8.06668616E+02   # Su(1)
   1000004     1.01310780E+03   # Su(2)
   1000006     1.01645887E+03   # Su(3)
   2000002     1.01715414E+03   # Su(4)
   2000004     1.05485067E+03   # Su(5)
   2000006     1.05485131E+03   # Su(6)
Block UMIX
  1  1     9.59297402E-01   # Re(UM(1,1))
  1  2    -2.82397758E-01   # Re(UM(1,2))
  2  1     2.82397758E-01   # Re(UM(2,1))
  2  2     9.59297402E-01   # Re(UM(2,2))
Block VMIX
  1  1     9.82029745E-01   # Re(UP(1,1))
  1  2    -1.88726202E-01   # Re(UP(1,2))
  2  1     1.88726202E-01   # Re(UP(2,1))
  2  2     9.82029745E-01   # Re(UP(2,2))
Block PSEUDOSCALARMIX
  1  1    -1.02749860E-01   # ZA(1,1)
  1  2     9.94707226E-01   # ZA(1,2)
  2  1     9.94707226E-01   # ZA(2,1)
  2  2     1.02749860E-01   # ZA(2,2)
Block DSQMIX
  1  1     0.00000000E+00   # ZD(1,1)
  1  2    -4.75934804E-17   # ZD(1,2)
  1  3    -9.76758678E-01   # ZD(1,3)
  1  4     0.00000000E+00   # ZD(1,4)
  1  5     2.68798043E-21   # ZD(1,5)
  1  6    -2.14341981E-01   # ZD(1,6)
  2  1    -0.00000000E+00   # ZD(2,1)
  2  2     2.16883995E-16   # ZD(2,2)
  2  3    -2.14341981E-01   # ZD(2,3)
  2  4    -0.00000000E+00   # ZD(2,4)
  2  5    -1.22491553E-20   # ZD(2,5)
  2  6     9.76758678E-01   # ZD(2,6)
  3  1     0.00000000E+00   # ZD(3,1)
  3  2    -4.66194455E-03   # ZD(3,2)
  3  3     0.00000000E+00   # ZD(3,3)
  3  4     0.00000000E+00   # ZD(3,4)
  3  5    -9.99989133E-01   # ZD(3,5)
  3  6     5.26988018E-19   # ZD(3,6)
  4  1     2.12932306E-04   # ZD(4,1)
  4  2     0.00000000E+00   # ZD(4,2)
  4  3     0.00000000E+00   # ZD(4,3)
  4  4     9.99999977E-01   # ZD(4,4)
  4  5     0.00000000E+00   # ZD(4,5)
  4  6     0.00000000E+00   # ZD(4,6)
  5  1     0.00000000E+00   # ZD(5,1)
  5  2     9.99989133E-01   # ZD(5,2)
  5  3     0.00000000E+00   # ZD(5,3)
  5  4     0.00000000E+00   # ZD(5,4)
  5  5    -4.66194455E-03   # ZD(5,5)
  5  6    -1.11021055E-16   # ZD(5,6)
  6  1     9.99999977E-01   # ZD(6,1)
  6  2     0.00000000E+00   # ZD(6,2)
  6  3     0.00000000E+00   # ZD(6,3)
  6  4    -2.12932306E-04   # ZD(6,4)
  6  5     0.00000000E+00   # ZD(6,5)
  6  6     0.00000000E+00   # ZD(6,6)
Block SELMIX
  1  1     0.00000000E+00   # ZE(1,1)
  1  2     0.00000000E+00   # ZE(1,2)
  1  3     1.42120159E-01   # ZE(1,3)
  1  4     0.00000000E+00   # ZE(1,4)
  1  5     0.00000000E+00   # ZE(1,5)
  1  6     9.89849413E-01   # ZE(1,6)
  2  1     0.00000000E+00   # ZE(2,1)
  2  2     8.51332488E-03   # ZE(2,2)
  2  3     0.00000000E+00   # ZE(2,3)
  2  4     0.00000000E+00   # ZE(2,4)
  2  5     9.99963761E-01   # ZE(2,5)
  2  6     0.00000000E+00   # ZE(2,6)
  3  1     4.11791172E-05   # ZE(3,1)
  3  2     0.00000000E+00   # ZE(3,2)
  3  3     0.00000000E+00   # ZE(3,3)
  3  4     9.99999999E-01   # ZE(3,4)
  3  5     0.00000000E+00   # ZE(3,5)
  3  6     0.00000000E+00   # ZE(3,6)
  4  1     9.99999999E-01   # ZE(4,1)
  4  2     0.00000000E+00   # ZE(4,2)
  4  3     0.00000000E+00   # ZE(4,3)
  4  4    -4.11791172E-05   # ZE(4,4)
  4  5     0.00000000E+00   # ZE(4,5)
  4  6     0.00000000E+00   # ZE(4,6)
  5  1     0.00000000E+00   # ZE(5,1)
  5  2     9.99963761E-01   # ZE(5,2)
  5  3     0.00000000E+00   # ZE(5,3)
  5  4     0.00000000E+00   # ZE(5,4)
  5  5    -8.51332488E-03   # ZE(5,5)
  5  6     0.00000000E+00   # ZE(5,6)
  6  1     0.00000000E+00   # ZE(6,1)
  6  2     0.00000000E+00   # ZE(6,2)
  6  3     9.89849413E-01   # ZE(6,3)
  6  4     0.00000000E+00   # ZE(6,4)
  6  5     0.00000000E+00   # ZE(6,5)
  6  6    -1.42120159E-01   # ZE(6,6)
Block SCALARMIX
  1  1     1.06581313E-01   # ZH(1,1)
  1  2     9.94303990E-01   # ZH(1,2)
  2  1     9.94303990E-01   # ZH(2,1)
  2  2    -1.06581313E-01   # ZH(2,2)
Block NMIX
  1  1    -9.95838295E-01   # Re(ZN(1,1))
  1  2     1.73982374E-02   # Re(ZN(1,2))
  1  3    -8.26522776E-02   # Re(ZN(1,3))
  1  4     3.42343826E-02   # Re(ZN(1,4))
  2  1     3.78678653E-02   # Re(ZN(2,1))
  2  2     9.70712039E-01   # Re(ZN(2,2))
  2  3    -1.97429986E-01   # Re(ZN(2,3))
  2  4     1.31550612E-01   # Re(ZN(2,4))
  3  1     3.31893152E-02   # Re(ZN(3,1))
  3  2    -4.83758514E-02   # Re(ZN(3,2))
  3  3    -7.03449808E-01   # Re(ZN(3,3))
  3  4    -7.08319571E-01   # Re(ZN(3,4))
  4  1     7.59643649E-02   # Re(ZN(4,1))
  4  2    -2.34681095E-01   # Re(ZN(4,2))
  4  3    -6.77752440E-01   # Re(ZN(4,3))
  4  4     6.92680178E-01   # Re(ZN(4,4))
Block CHARGEMIX
  1  1    -1.03090008E-01   # ZP(1,1)
  1  2     9.94672032E-01   # ZP(1,2)
  2  1     9.94672032E-01   # ZP(2,1)
  2  2     1.03090008E-01   # ZP(2,2)
Block USQMIX
  1  1     0.00000000E+00   # ZU(1,1)
  1  2     0.00000000E+00   # ZU(1,2)
  1  3     4.26615768E-01   # ZU(1,3)
  1  4     0.00000000E+00   # ZU(1,4)
  1  5    -2.25524290E-15   # ZU(1,5)
  1  6     9.04432964E-01   # ZU(1,6)
  2  1     0.00000000E+00   # ZU(2,1)
  2  2     0.00000000E+00   # ZU(2,2)
  2  3     9.04432964E-01   # ZU(2,3)
  2  4     0.00000000E+00   # ZU(2,4)
  2  5    -4.81939730E-15   # ZU(2,5)
  2  6    -4.26615768E-01   # ZU(2,6)
  3  1     0.00000000E+00   # ZU(3,1)
  3  2     9.46254165E-03   # ZU(3,2)
  3  3     5.10679727E-15   # ZU(3,3)
  3  4     0.00000000E+00   # ZU(3,4)
  3  5     9.99955229E-01   # ZU(3,5)
  3  6     0.00000000E+00   # ZU(3,6)
  4  1     2.07063630E-05   # ZU(4,1)
  4  2     0.00000000E+00   # ZU(4,2)
  4  3     0.00000000E+00   # ZU(4,3)
  4  4     1.00000000E+00   # ZU(4,4)
  4  5     0.00000000E+00   # ZU(4,5)
  4  6     0.00000000E+00   # ZU(4,6)
  5  1     1.00000000E+00   # ZU(5,1)
  5  2     0.00000000E+00   # ZU(5,2)
  5  3     0.00000000E+00   # ZU(5,3)
  5  4    -2.07063630E-05   # ZU(5,4)
  5  5     0.00000000E+00   # ZU(5,5)
  5  6     0.00000000E+00   # ZU(5,6)
  6  1     0.00000000E+00   # ZU(6,1)
  6  2    -9.99955229E-01   # ZU(6,2)
  6  3     4.83254454E-17   # ZU(6,3)
  6  4     0.00000000E+00   # ZU(6,4)
  6  5     9.46254165E-03   # ZU(6,5)
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
Block ALPHA Q= 8.76740936E+02
           1.06784138E-01   # ArcCos(Pole(ZH(0,1)))
Block HMIX Q= 8.76740936E+02
     1     6.31218393E+02   # Mu
     2     9.67312621E+00   # vu/vd
     3     2.44053433E+02   # Sqrt(Sqr(vd) + Sqr(vu))
     4     5.36777230E+05   # Sqr(MAh(1))
   101     5.49048159E+04   # BMu
   102     2.50962986E+01   # vd
   103     2.42759663E+02   # vu
Block Au Q= 8.76740936E+02
  1  1    -1.14477419E+03   # TYu(0,0)/Yu(0,0)
  2  2    -1.14476911E+03   # TYu(1,1)/Yu(1,1)
  3  3    -8.83902977E+02   # TYu(2,2)/Yu(2,2)
Block Ad Q= 8.76740936E+02
  1  1    -1.40026447E+03   # TYd(0,0)/Yd(0,0)
  2  2    -1.40025976E+03   # TYd(1,1)/Yd(1,1)
  3  3    -1.30885006E+03   # TYd(2,2)/Yd(2,2)
Block Ae Q= 8.76740936E+02
  1  1    -3.00005426E+02   # TYe(0,0)/Ye(0,0)
  2  2    -3.00000006E+02   # TYe(1,1)/Ye(1,1)
  3  3    -2.98364373E+02   # TYe(2,2)/Ye(2,2)
Block MSOFT Q= 8.76740936E+02
     1     2.09018579E+02   # MassB
     2     3.88257873E+02   # MassWB
     3     1.11544211E+03   # MassG
    21     1.09683411E+05   # mHd2
    22    -3.85898988E+05   # mHu2
    31     3.54416224E+02   # Sqrt(ml2(0,0))
    32     3.54412891E+02   # Sqrt(ml2(1,1))
    33     3.53407333E+02   # Sqrt(ml2(2,2))
    34     2.22035720E+02   # Sqrt(me2(0,0))
    35     2.22024873E+02   # Sqrt(me2(1,1))
    36     2.18731935E+02   # Sqrt(me2(2,2))
    41     1.02053367E+03   # Sqrt(mq2(0,0))
    42     1.02053107E+03   # Sqrt(mq2(1,1))
    43     9.40760849E+02   # Sqrt(mq2(2,2))
    44     9.82565930E+02   # Sqrt(mu2(0,0))
    45     9.82563167E+02   # Sqrt(mu2(1,1))
    46     8.09126983E+02   # Sqrt(mu2(2,2))
    47     9.77979392E+02   # Sqrt(md2(0,0))
    48     9.77976666E+02   # Sqrt(md2(1,1))
    49     9.73121951E+02   # Sqrt(md2(2,2))
