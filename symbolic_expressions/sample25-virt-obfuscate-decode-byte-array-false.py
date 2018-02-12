#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_73922 = ref_278 # MOV operation
ref_73998 = ref_73922 # MOV operation
ref_74012 = (ref_73998 >> (0x33 & 0x3F)) # SHR operation
ref_74850 = ref_278 # MOV operation
ref_75050 = ref_74850 # MOV operation
ref_75058 = ((ref_75050 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_75065 = ref_75058 # MOV operation
ref_75161 = ref_75065 # MOV operation
ref_75173 = ref_74012 # MOV operation
ref_75175 = (ref_75173 | ref_75161) # OR operation
ref_76106 = ref_75175 # MOV operation
ref_77055 = ref_278 # MOV operation
ref_77131 = ref_77055 # MOV operation
ref_77147 = ((((0x0) << 64 | ref_77131) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_77368 = ref_77147 # MOV operation
ref_77374 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_77368)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_78302 = ref_77374 # MOV operation
ref_79220 = ref_78302 # MOV operation
ref_80118 = ref_76106 # MOV operation
ref_80194 = ref_80118 # MOV operation
ref_80206 = ref_79220 # MOV operation
ref_80208 = (ref_80206 | ref_80194) # OR operation
ref_81046 = ref_278 # MOV operation
ref_81122 = ref_81046 # MOV operation
ref_81134 = ref_80208 # MOV operation
ref_81136 = ((ref_81134 + ref_81122) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_82068 = ref_81136 # MOV operation
ref_83334 = ref_76106 # MOV operation
ref_83410 = ref_83334 # MOV operation
ref_83424 = ((ref_83410 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_83432 = ref_83424 # MOV operation
ref_83656 = ref_83432 # MOV operation
ref_83658 = ((0x28E5FC28 - ref_83656) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_83666 = ref_83658 # MOV operation
ref_83762 = ref_83666 # MOV operation
ref_83776 = (ref_83762 >> (0x2 & 0x3F)) # SHR operation
ref_84001 = ref_83776 # MOV operation
ref_84007 = (0x7 & ref_84001) # AND operation
ref_84108 = ref_84007 # MOV operation
ref_84122 = (0x1 | ref_84108) # OR operation
ref_85045 = ref_78302 # MOV operation
ref_85858 = ref_278 # MOV operation
ref_85934 = ref_85858 # MOV operation
ref_85946 = ref_85045 # MOV operation
ref_85948 = ((ref_85946 + ref_85934) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_86050 = ref_85948 # MOV operation
ref_86062 = ref_84122 # MOV operation
ref_86064 = (ref_86050 >> ((ref_86062 & 0xFF) & 0x3F)) # SHR operation
ref_86995 = ref_86064 # MOV operation
ref_88145 = ref_86995 # MOV operation
ref_88221 = ref_88145 # MOV operation
ref_88235 = (ref_88221 >> (0x1 & 0x3F)) # SHR operation
ref_88460 = ref_88235 # MOV operation
ref_88466 = (0x7 & ref_88460) # AND operation
ref_88567 = ref_88466 # MOV operation
ref_88581 = (0x1 | ref_88567) # OR operation
ref_89504 = ref_86995 # MOV operation
ref_89580 = ref_89504 # MOV operation
ref_89592 = ref_88581 # MOV operation
ref_89594 = (ref_89580 >> ((ref_89592 & 0xFF) & 0x3F)) # SHR operation
ref_90525 = ref_89594 # MOV operation
ref_90527 = ((ref_90525 >> 56) & 0xFF) # Byte reference - MOV operation
ref_90528 = ((ref_90525 >> 48) & 0xFF) # Byte reference - MOV operation
ref_90529 = ((ref_90525 >> 40) & 0xFF) # Byte reference - MOV operation
ref_90530 = ((ref_90525 >> 32) & 0xFF) # Byte reference - MOV operation
ref_90531 = ((ref_90525 >> 24) & 0xFF) # Byte reference - MOV operation
ref_90532 = ((ref_90525 >> 16) & 0xFF) # Byte reference - MOV operation
ref_90533 = ((ref_90525 >> 8) & 0xFF) # Byte reference - MOV operation
ref_90534 = (ref_90525 & 0xFF) # Byte reference - MOV operation
ref_92516 = ref_76106 # MOV operation
ref_92716 = ref_92516 # MOV operation
ref_92722 = (0x7 & ref_92716) # AND operation
ref_92947 = ref_92722 # MOV operation
ref_92955 = ((ref_92947 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_92962 = ref_92955 # MOV operation
ref_93880 = ref_82068 # MOV operation
ref_93956 = ref_93880 # MOV operation
ref_93968 = ref_92962 # MOV operation
ref_93970 = (ref_93968 | ref_93956) # OR operation
ref_94901 = ref_93970 # MOV operation
ref_96425 = ((((ref_90527) << 8 | ref_90528) << 8 | ref_90529) << 8 | ref_90530) # MOV operation
ref_96633 = (ref_96425 & 0xFFFFFFFF) # MOV operation
ref_98153 = ((((ref_90531) << 8 | ref_90532) << 8 | ref_90533) << 8 | ref_90534) # MOV operation
ref_99661 = (ref_98153 & 0xFFFFFFFF) # MOV operation
ref_99881 = (ref_96633 & 0xFFFFFFFF) # MOV operation
ref_101389 = (ref_99881 & 0xFFFFFFFF) # MOV operation
ref_103696 = ref_94901 # MOV operation
ref_103896 = ref_103696 # MOV operation
ref_103902 = (0x7 & ref_103896) # AND operation
ref_104127 = ref_103902 # MOV operation
ref_104135 = ((ref_104127 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_104142 = ref_104135 # MOV operation
ref_105060 = ref_94901 # MOV operation
ref_105136 = ref_105060 # MOV operation
ref_105148 = ref_104142 # MOV operation
ref_105150 = (ref_105148 | ref_105136) # OR operation
ref_106081 = ref_105150 # MOV operation
ref_107605 = (ref_99661 & 0xFFFFFFFF) # MOV operation
ref_107813 = (ref_107605 & 0xFFFFFFFF) # MOV operation
ref_109333 = (ref_101389 & 0xFFFFFFFF) # MOV operation
ref_110841 = (ref_109333 & 0xFFFFFFFF) # MOV operation
ref_110843 = (((ref_110841 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_110844 = (((ref_110841 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_110845 = (((ref_110841 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_110846 = ((ref_110841 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_111061 = (ref_107813 & 0xFFFFFFFF) # MOV operation
ref_112569 = (ref_111061 & 0xFFFFFFFF) # MOV operation
ref_112571 = (((ref_112569 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_112572 = (((ref_112569 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_112573 = (((ref_112569 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_112574 = ((ref_112569 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_115065 = ref_106081 # MOV operation
ref_115963 = ((((((((ref_110843) << 8 | ref_110844) << 8 | ref_110845) << 8 | ref_110846) << 8 | ref_112571) << 8 | ref_112572) << 8 | ref_112573) << 8 | ref_112574) # MOV operation
ref_116163 = ref_115963 # MOV operation
ref_116169 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_116163)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_116275 = ref_115065 # MOV operation
ref_116279 = ref_116169 # MOV operation
ref_116281 = (ref_116279 ^ ref_116275) # XOR operation
ref_116506 = ref_116281 # MOV operation
ref_116512 = (0xF & ref_116506) # AND operation
ref_116613 = ref_116512 # MOV operation
ref_116627 = (0x1 | ref_116613) # OR operation
ref_116856 = ref_116627 # MOV operation
ref_116858 = ((0x40 - ref_116856) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_116866 = ref_116858 # MOV operation
ref_117784 = ref_76106 # MOV operation
ref_118682 = ref_78302 # MOV operation
ref_118766 = ref_117784 # MOV operation
ref_118770 = ref_118682 # MOV operation
ref_118772 = (((sx(0x40, ref_118770) * sx(0x40, ref_118766)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_118870 = ref_118772 # MOV operation
ref_118882 = ref_116866 # MOV operation
ref_118884 = (ref_118870 >> ((ref_118882 & 0xFF) & 0x3F)) # SHR operation
ref_119807 = ref_76106 # MOV operation
ref_120705 = ref_78302 # MOV operation
ref_120789 = ref_119807 # MOV operation
ref_120793 = ref_120705 # MOV operation
ref_120795 = (((sx(0x40, ref_120793) * sx(0x40, ref_120789)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_121831 = ref_106081 # MOV operation
ref_122729 = ((((((((ref_110843) << 8 | ref_110844) << 8 | ref_110845) << 8 | ref_110846) << 8 | ref_112571) << 8 | ref_112572) << 8 | ref_112573) << 8 | ref_112574) # MOV operation
ref_122929 = ref_122729 # MOV operation
ref_122935 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_122929)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_123041 = ref_121831 # MOV operation
ref_123045 = ref_122935 # MOV operation
ref_123047 = (ref_123045 ^ ref_123041) # XOR operation
ref_123272 = ref_123047 # MOV operation
ref_123278 = (0xF & ref_123272) # AND operation
ref_123379 = ref_123278 # MOV operation
ref_123393 = (0x1 | ref_123379) # OR operation
ref_123502 = ref_120795 # MOV operation
ref_123506 = ref_123393 # MOV operation
ref_123508 = (ref_123506 & 0xFFFFFFFF) # MOV operation
ref_123510 = ((ref_123502 << ((ref_123508 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_123517 = ref_123510 # MOV operation
ref_123613 = ref_123517 # MOV operation
ref_123625 = ref_118884 # MOV operation
ref_123627 = (ref_123625 | ref_123613) # OR operation
ref_124482 = ref_123627 # MOV operation
ref_124693 = ref_124482 # MOV operation
ref_124695 = ref_124693 # MOV operation

print ref_124695 & 0xffffffffffffffff