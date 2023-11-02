from konlpy.tag import Hannanum

hannanum = Hannanum()
test_txt= "11월 3일 13시 30분"
print(hannanum.analyze(test_txt))


print(hannanum.morphs(test_txt))


print(hannanum.nouns(test_txt))


print(hannanum.pos(test_txt))