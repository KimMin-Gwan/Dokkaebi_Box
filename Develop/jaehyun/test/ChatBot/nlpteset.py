from konlpy.tag import Hannanum, Okt

hannanum = Hannanum()
Okt = Okt()
test_txt= "우리 집앞 영남대에서 주웠어"
print(hannanum.analyze(test_txt))
print(hannanum.morphs(test_txt))
print(hannanum.nouns(test_txt))
print(hannanum.pos(test_txt))

print(Okt.morphs(test_txt))
print(Okt.nouns(test_txt))