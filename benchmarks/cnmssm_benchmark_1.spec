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
     1     2.00000000E+02   # m0
     2     2.00000000E+02   # m12
     3     1.00000000E+01   # TanBeta
     4                  1   # SignvS
     5    -5.00000000E+02   # Azero
Block EXTPAR
    61     1.00000000E-01   # LambdaInput
Block gauge Q= 3.43058470E+02
     1     3.59966917E-01   # gY
     2     6.46299225E-01   # g2
     3     1.11192122E+00   # g3
Block Yu Q= 3.43058470E+02
  1  1     7.55632385E-06   # Yu(1,1)
  1  2     0.00000000E+00   # Yu(1,2)
  1  3     0.00000000E+00   # Yu(1,3)
  2  1     0.00000000E+00   # Yu(2,1)
  2  2     3.45362689E-03   # Yu(2,2)
  2  3     0.00000000E+00   # Yu(2,3)
  3  1     0.00000000E+00   # Yu(3,1)
  3  2     0.00000000E+00   # Yu(3,2)
  3  3     8.90163220E-01   # Yu(3,3)
Block Yd Q= 3.43058470E+02
  1  1     1.47307572E-04   # Yd(1,1)
  1  2     0.00000000E+00   # Yd(1,2)
  1  3     0.00000000E+00   # Yd(1,3)
  2  1     0.00000000E+00   # Yd(2,1)
  2  2     3.22526177E-03   # Yd(2,2)
  2  3     0.00000000E+00   # Yd(2,3)
  3  1     0.00000000E+00   # Yd(3,1)
  3  2     0.00000000E+00   # Yd(3,2)
  3  3     1.37927883E-01   # Yd(3,3)
Block Ye Q= 3.43058470E+02
  1  1     2.82924785E-05   # Ye(1,1)
  1  2     0.00000000E+00   # Ye(1,2)
  1  3     0.00000000E+00   # Ye(1,3)
  2  1     0.00000000E+00   # Ye(2,1)
  2  2     5.84999185E-03   # Ye(2,2)
  2  3     0.00000000E+00   # Ye(2,3)
  3  1     0.00000000E+00   # Ye(3,1)
  3  2     0.00000000E+00   # Ye(3,2)
  3  3     1.01071763E-01   # Ye(3,3)
Block Te Q= 3.43058470E+02
  1  1    -1.74718393E-02   # TYe(1,1)
  1  2     0.00000000E+00   # TYe(1,2)
  1  3     0.00000000E+00   # TYe(1,3)
  2  1     0.00000000E+00   # TYe(2,1)
  2  2    -3.61252433E+00   # TYe(2,2)
  2  3     0.00000000E+00   # TYe(2,3)
  3  1     0.00000000E+00   # TYe(3,1)
  3  2     0.00000000E+00   # TYe(3,2)
  3  3    -6.18967060E+01   # TYe(3,3)
Block Td Q= 3.43058470E+02
  1  1    -1.65316532E-01   # TYd(1,1)
  1  2     0.00000000E+00   # TYd(1,2)
  1  3     0.00000000E+00   # TYd(1,3)
  2  1     0.00000000E+00   # TYd(2,1)
  2  2    -3.61954622E+00   # TYd(2,2)
  2  3     0.00000000E+00   # TYd(2,3)
  3  1     0.00000000E+00   # TYd(3,1)
  3  2     0.00000000E+00   # TYd(3,2)
  3  3    -1.40795881E+02   # TYd(3,3)
Block Tu Q= 3.43058470E+02
  1  1    -6.32498002E-03   # TYu(1,1)
  1  2     0.00000000E+00   # TYu(1,2)
  1  3     0.00000000E+00   # TYu(1,3)
  2  1     0.00000000E+00   # TYu(2,1)
  2  2    -2.89082028E+00   # TYu(2,2)
  2  3     0.00000000E+00   # TYu(2,3)
  3  1     0.00000000E+00   # TYu(3,1)
  3  2     0.00000000E+00   # TYu(3,2)
  3  3    -4.88221681E+02   # TYu(3,3)
Block MSQ2 Q= 3.43058470E+02
  1  1     2.32982490E+05   # mq2(1,1)
  1  2     0.00000000E+00   # mq2(1,2)
  1  3     0.00000000E+00   # mq2(1,3)
  2  1     0.00000000E+00   # mq2(2,1)
  2  2     2.32979524E+05   # mq2(2,2)
  2  3     0.00000000E+00   # mq2(2,3)
  3  1     0.00000000E+00   # mq2(3,1)
  3  2     0.00000000E+00   # mq2(3,2)
  3  3     1.68382760E+05   # mq2(3,3)
Block MSE2 Q= 3.43058470E+02
  1  1     4.53428532E+04   # me2(1,1)
  1  2     0.00000000E+00   # me2(1,2)
  1  3     0.00000000E+00   # me2(1,3)
  2  1     0.00000000E+00   # me2(2,1)
  2  2     4.53333270E+04   # me2(2,2)
  2  3     0.00000000E+00   # me2(2,3)
  3  1     0.00000000E+00   # me2(3,1)
  3  2     0.00000000E+00   # me2(3,2)
  3  3     4.25172186E+04   # me2(3,3)
Block MSL2 Q= 3.43058470E+02
  1  1     5.79262624E+04   # ml2(1,1)
  1  2     0.00000000E+00   # ml2(1,2)
  1  3     0.00000000E+00   # ml2(1,3)
  2  1     0.00000000E+00   # ml2(2,1)
  2  2     5.79215405E+04   # ml2(2,2)
  2  3     0.00000000E+00   # ml2(2,3)
  3  1     0.00000000E+00   # ml2(3,1)
  3  2     0.00000000E+00   # ml2(3,2)
  3  3     5.65259412E+04   # ml2(3,3)
Block MSU2 Q= 3.43058470E+02
  1  1     2.20754452E+05   # mu2(1,1)
  1  2     0.00000000E+00   # mu2(1,2)
  1  3     0.00000000E+00   # mu2(1,3)
  2  1     0.00000000E+00   # mu2(2,1)
  2  2     2.20751684E+05   # mu2(2,2)
  2  3     0.00000000E+00   # mu2(2,3)
  3  1     0.00000000E+00   # mu2(3,1)
  3  2     0.00000000E+00   # mu2(3,2)
  3  3     9.38916528E+04   # mu2(3,3)
Block MSD2 Q= 3.43058470E+02
  1  1     2.19406953E+05   # md2(1,1)
  1  2     0.00000000E+00   # md2(1,2)
  1  3     0.00000000E+00   # md2(1,3)
  2  1     0.00000000E+00   # md2(2,1)
  2  2     2.19403729E+05   # md2(2,2)
  2  3     0.00000000E+00   # md2(2,3)
  3  1     0.00000000E+00   # md2(3,1)
  3  2     0.00000000E+00   # md2(3,2)
  3  3     2.14017987E+05   # md2(3,3)
Block MSOFT Q= 3.43058470E+02
    21     4.74655206E+04   # mHd2
    22    -1.47878912E+05   # mHu2
     1     8.07538452E+01   # MassB
     2     1.53291759E+02   # MassWB
     3     4.81135148E+02   # MassG
Block HMIX Q= 3.43058470E+02
   102     2.49301218E+01   # vd
   103     2.44232315E+02   # vu
Block NMSSMRUN Q= 3.43058470E+02
     2     9.08573087E-02   # Kappa
     4    -4.34872152E+01   # TKappa
     1     1.01141968E-01   # Lambdax
     3    -2.91347868E+01   # TLambdax
    10    -6.98403943E+04   # ms2
     5     5.31167741E+03   # vS
Block MASS
   1000021     5.04417179E+02   # Glu
        24     8.04040000E+01   # VWm
   1000024     1.46650870E+02   # Cha(1)
   1000037     3.99720039E+02   # Cha(2)
        37     4.44303782E+02   # Hpm(2)
        25     1.10156070E+02   # hh(1)
        35     4.36135471E+02   # hh(2)
        45     5.50698799E+02   # hh(3)
   1000012     2.29216952E+02   # Sv(1)
   1000014     2.32281594E+02   # Sv(2)
   1000016     2.32291888E+02   # Sv(3)
        36     4.36172901E+02   # Ah(2)
        46     7.00773192E+02   # Ah(3)
   1000022     7.78536366E+01   # Chi(1)
   1000023     1.46876130E+02   # Chi(2)
   1000025    -3.86880492E+02   # Chi(3)
   1000035     3.95073202E+02   # Chi(4)
   1000045     6.83077648E+02   # Chi(5)
   1000001     4.22841968E+02   # Sd(1)
   1000003     4.79660346E+02   # Sd(2)
   1000005     4.82541099E+02   # Sd(3)
   2000001     4.82549253E+02   # Sd(4)
   2000003     4.99330174E+02   # Sd(5)
   2000005     4.99331753E+02   # Sd(6)
   1000011     2.02838946E+02   # Se(1)
   1000013     2.17697461E+02   # Se(2)
   1000015     2.17755859E+02   # Se(3)
   2000011     2.45494555E+02   # Se(4)
   2000013     2.45516965E+02   # Se(5)
   2000015     2.49523876E+02   # Se(6)
   1000002     2.50606626E+02   # Su(1)
   1000004     4.81935504E+02   # Su(2)
   1000006     4.81965365E+02   # Su(3)
   2000002     4.93213415E+02   # Su(4)
   2000004     4.93237469E+02   # Su(5)
   2000006     5.11858229E+02   # Su(6)
Block UMIX
  1  1     9.40935754E-01   # Re(UM(1,1))
  1  2    -3.38585153E-01   # Re(UM(1,2))
  2  1     3.38585153E-01   # Re(UM(2,1))
  2  2     9.40935754E-01   # Re(UM(2,2))
Block VMIX
  1  1     9.87018467E-01   # Re(UP(1,1))
  1  2    -1.60606806E-01   # Re(UP(1,2))
  2  1     1.60606806E-01   # Re(UP(2,1))
  2  2     9.87018467E-01   # Re(UP(2,2))
Block NMAMIX
  1  1     1.01536488E-01   # ZA(1,1)
  1  2    -9.94831816E-01   # ZA(1,2)
  1  3    -1.01955628E-06   # ZA(1,3)
  2  1    -9.93219692E-01   # ZA(2,1)
  2  2    -1.01371890E-01   # ZA(2,2)
  2  3    -5.69067924E-02   # ZA(2,3)
  3  1     5.66125843E-02   # ZA(3,1)
  3  2     5.77912847E-03   # ZA(3,2)
  3  3    -9.98379495E-01   # ZA(3,3)
Block DSQMIX
  1  1    -0.00000000E+00   # ZD(1,1)
  1  2    -0.00000000E+00   # ZD(1,2)
  1  3    -9.73793693E-01   # ZD(1,3)
  1  4    -0.00000000E+00   # ZD(1,4)
  1  5     9.61973515E-14   # ZD(1,5)
  1  6    -2.27433165E-01   # ZD(1,6)
  2  1     0.00000000E+00   # ZD(2,1)
  2  2     0.00000000E+00   # ZD(2,2)
  2  3     2.27433165E-01   # ZD(2,3)
  2  4     0.00000000E+00   # ZD(2,4)
  2  5    -2.24719487E-14   # ZD(2,5)
  2  6    -9.73793693E-01   # ZD(2,6)
  3  1     0.00000000E+00   # ZD(3,1)
  3  2     1.71319409E-02   # ZD(3,2)
  3  3     9.85733356E-14   # ZD(3,3)
  3  4     0.00000000E+00   # ZD(3,4)
  3  5     9.99853238E-01   # ZD(3,5)
  3  6     0.00000000E+00   # ZD(3,6)
  4  1     7.82822999E-04   # ZD(4,1)
  4  2     0.00000000E+00   # ZD(4,2)
  4  3     0.00000000E+00   # ZD(4,3)
  4  4     9.99999694E-01   # ZD(4,4)
  4  5     0.00000000E+00   # ZD(4,5)
  4  6     0.00000000E+00   # ZD(4,6)
  5  1     9.99999694E-01   # ZD(5,1)
  5  2     0.00000000E+00   # ZD(5,2)
  5  3     0.00000000E+00   # ZD(5,3)
  5  4    -7.82822999E-04   # ZD(5,4)
  5  5     0.00000000E+00   # ZD(5,5)
  5  6     0.00000000E+00   # ZD(5,6)
  6  1     0.00000000E+00   # ZD(6,1)
  6  2    -9.99853238E-01   # ZD(6,2)
  6  3     1.68900044E-15   # ZD(6,3)
  6  4     0.00000000E+00   # ZD(6,4)
  6  5     1.71319409E-02   # ZD(6,5)
  6  6     0.00000000E+00   # ZD(6,6)
Block SELMIX
  1  1     0.00000000E+00   # ZE(1,1)
  1  2     0.00000000E+00   # ZE(1,2)
  1  3     4.01725290E-01   # ZE(1,3)
  1  4     0.00000000E+00   # ZE(1,4)
  1  5     0.00000000E+00   # ZE(1,5)
  1  6     9.15760226E-01   # ZE(1,6)
  2  1     0.00000000E+00   # ZE(2,1)
  2  2     3.49529539E-02   # ZE(2,2)
  2  3     0.00000000E+00   # ZE(2,3)
  2  4     0.00000000E+00   # ZE(2,4)
  2  5     9.99388959E-01   # ZE(2,5)
  2  6     0.00000000E+00   # ZE(2,6)
  3  1     1.69419542E-04   # ZE(3,1)
  3  2     0.00000000E+00   # ZE(3,2)
  3  3     0.00000000E+00   # ZE(3,3)
  3  4     9.99999986E-01   # ZE(3,4)
  3  5     0.00000000E+00   # ZE(3,5)
  3  6     0.00000000E+00   # ZE(3,6)
  4  1     9.99999986E-01   # ZE(4,1)
  4  2     0.00000000E+00   # ZE(4,2)
  4  3     0.00000000E+00   # ZE(4,3)
  4  4    -1.69419542E-04   # ZE(4,4)
  4  5     0.00000000E+00   # ZE(4,5)
  4  6     0.00000000E+00   # ZE(4,6)
  5  1     0.00000000E+00   # ZE(5,1)
  5  2     9.99388959E-01   # ZE(5,2)
  5  3     0.00000000E+00   # ZE(5,3)
  5  4     0.00000000E+00   # ZE(5,4)
  5  5    -3.49529539E-02   # ZE(5,5)
  5  6     0.00000000E+00   # ZE(5,6)
  6  1     0.00000000E+00   # ZE(6,1)
  6  2     0.00000000E+00   # ZE(6,2)
  6  3     9.15760226E-01   # ZE(6,3)
  6  4     0.00000000E+00   # ZE(6,4)
  6  5     0.00000000E+00   # ZE(6,5)
  6  6    -4.01725290E-01   # ZE(6,6)
Block NMHMIX
  1  1     1.08273978E-01   # ZH(1,1)
  1  2     9.93295441E-01   # ZH(1,2)
  1  3    -4.05081822E-02   # ZH(1,3)
  2  1     9.92529903E-01   # ZH(2,1)
  2  2    -1.05706345E-01   # ZH(2,2)
  2  3     6.09143675E-02   # ZH(2,3)
  3  1    -5.62239916E-02   # ZH(3,1)
  3  2     4.68010230E-02   # ZH(3,2)
  3  3     9.97320674E-01   # ZH(3,3)
Block NMNMIX
  1  1     9.88209014E-01   # Re(ZN(1,1))
  1  2    -5.66206576E-02   # Re(ZN(1,2))
  1  3     1.35950792E-01   # Re(ZN(1,3))
  1  4    -4.16946398E-02   # Re(ZN(1,4))
  1  5     3.99812467E-03   # Re(ZN(1,5))
  2  1    -9.16852357E-02   # Re(ZN(2,1))
  2  2    -9.62176436E-01   # Re(ZN(2,2))
  2  3     2.32018458E-01   # Re(ZN(2,3))
  2  4    -1.09209212E-01   # Re(ZN(2,4))
  2  5     7.14884243E-03   # Re(ZN(2,5))
  3  1    -6.03161306E-02   # Re(ZN(3,1))
  3  2     9.26749028E-02   # Re(ZN(3,2))
  3  3     6.94628485E-01   # Re(ZN(3,3))
  3  4     7.10710580E-01   # Re(ZN(3,4))
  3  5     1.24525455E-02   # Re(ZN(3,5))
  4  1    -1.06756307E-01   # Re(ZN(4,1))
  4  2     2.49823925E-01   # Re(ZN(4,2))
  4  3     6.66287737E-01   # Re(ZN(4,3))
  4  4    -6.93486093E-01   # Re(ZN(4,4))
  4  5     3.64525412E-02   # Re(ZN(4,5))
  5  1     1.34813435E-03   # Re(ZN(5,1))
  5  2    -3.15838135E-03   # Re(ZN(5,2))
  5  3    -3.51672674E-02   # Re(ZN(5,3))
  5  4     1.73900852E-02   # Re(ZN(5,4))
  5  5     9.99224227E-01   # Re(ZN(5,5))
Block CHARGEMIX
  1  1    -1.01636021E-01   # ZP(1,1)
  1  2     9.94821652E-01   # ZP(1,2)
  2  1     9.94821652E-01   # ZP(2,1)
  2  2     1.01636021E-01   # ZP(2,2)
Block USQMIX
  1  1    -0.00000000E+00   # ZU(1,1)
  1  2    -0.00000000E+00   # ZU(1,2)
  1  3     5.59387376E-01   # ZU(1,3)
  1  4    -0.00000000E+00   # ZU(1,4)
  1  5     2.81980833E-14   # ZU(1,5)
  1  6     8.28906366E-01   # ZU(1,6)
  2  1     0.00000000E+00   # ZU(2,1)
  2  2    -4.86654491E-02   # ZU(2,2)
  2  3     5.01226217E-14   # ZU(2,3)
  2  4     0.00000000E+00   # ZU(2,4)
  2  5    -9.98815135E-01   # ZU(2,5)
  2  6     0.00000000E+00   # ZU(2,6)
  3  1     1.06856194E-04   # ZU(3,1)
  3  2     0.00000000E+00   # ZU(3,2)
  3  3     0.00000000E+00   # ZU(3,3)
  3  4     9.99999994E-01   # ZU(3,4)
  3  5     0.00000000E+00   # ZU(3,5)
  3  6     0.00000000E+00   # ZU(3,6)
  4  1     9.99999994E-01   # ZU(4,1)
  4  2     0.00000000E+00   # ZU(4,2)
  4  3     0.00000000E+00   # ZU(4,3)
  4  4    -1.06856194E-04   # ZU(4,4)
  4  5     0.00000000E+00   # ZU(4,5)
  4  6     0.00000000E+00   # ZU(4,6)
  5  1     0.00000000E+00   # ZU(5,1)
  5  2    -9.98815135E-01   # ZU(5,2)
  5  3    -2.44213349E-15   # ZU(5,3)
  5  4     0.00000000E+00   # ZU(5,4)
  5  5     4.86654491E-02   # ZU(5,5)
  5  6     0.00000000E+00   # ZU(5,6)
  6  1     0.00000000E+00   # ZU(6,1)
  6  2     0.00000000E+00   # ZU(6,2)
  6  3     8.28906366E-01   # ZU(6,3)
  6  4     0.00000000E+00   # ZU(6,4)
  6  5     4.17751545E-14   # ZU(6,5)
  6  6    -5.59387376E-01   # ZU(6,6)
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