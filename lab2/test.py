# Author: Alex

# 相似度计算

print("\t\t== 相似度计算 ==\n")


h1 = "SdETTGHWeLICKSTGUKtESOTV3KKCPadA"
h2 = "OSnR5KQJP2ERVNqpRUCPSFX9KJFTSFVK"
h3 = "AAJHUTFOPAGaGK0VMrETKXLWefPOSRNE"
h4 = "IPOSOX2PUFJFJQaHgGJtVKUWJgVQFaI9"
h5 = "VBNWB0TVFVHLMIEDNNHUIDBrQUeLIDJs"
h6 = "VDPVbOoMLaSFrJHSRdXgLRBMLObOGSHQ"
h7 = "aHKSFT6a2NgUOKOPa3RVMeBUWAJEEcrO"
h8 = "LEDENKNFUUKPeJUc1AOPs4VFXV0UMSJW"
h9 = "dVoKbUEIGNaJ9BTPEbRHpGPItIXMKMKP"
h10 = "K7ENRTP5NsQDJFJMWLBOOQDOUrDPRfUT"


list_h =[h2, h3, h4, h5, h6, h7, h8, h8, h10]

li_1 = list(h1)
a = 0
for i in range(0, len(list_h)):
    li = list(list_h[i])
    for j in range(0, 31):
        if li_1[j] == li[j]:
            a += 1

    print("h1和h{}的相似度:\t\t".format(i+2), (a/32)*10, "%")



