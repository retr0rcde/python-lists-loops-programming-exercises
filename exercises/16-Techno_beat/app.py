

# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))



def lyrics_generator(beat_list):
    lyrics = []
    count = 0

    for beat in beat_list:
        if beat == 0:
            lyrics.append("Boom")
            count = 0
        elif beat == 1:
            lyrics.append("Drop the bass")
            count += 1
            if count == 3:
                lyrics.append("!!!Break the bass!!!")
                count = 0
    
    return lyrics


