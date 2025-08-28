import random

def player(prev_play, opponent_history=[], play_order={}):
    # Rakibin hamlesini kaydet
    if prev_play != "":
        opponent_history.append(prev_play)

    # Tahmin edilecek hamle (default)
    guess = "R"

    # Pattern boyutları: en uzun önce
    for n in [6,5,4,3,2,1]:
        if len(opponent_history) > n:
            last_pattern = "".join(opponent_history[-n:])
            if last_pattern not in play_order:
                play_order[last_pattern] = {"R":0,"P":0,"S":0}

            # Geçmişte n+1 uzunlukta pattern bul
            for i in range(len(opponent_history)-n):
                pattern = "".join(opponent_history[i:i+n])
                next_move = opponent_history[i+n]
                if pattern == last_pattern:
                    play_order[last_pattern][next_move] += 1

            # Pattern için veri varsa tahmin et
            if sum(play_order[last_pattern].values()) > 0:
                predicted_move = max(play_order[last_pattern], key=play_order[last_pattern].get)
                if predicted_move == "R":
                    return "P"
                elif predicted_move == "P":
                    return "S"
                elif predicted_move == "S":
                    return "R"

    # Pattern bulunamazsa weighted fallback: geçmiş tüm hamleler
    if opponent_history:
        counts = {"R":0,"P":0,"S":0}
        for move in opponent_history:
            counts[move] += 1

        # Toplam hamle sayısı
        total = sum(counts.values())
        if total > 0:
            # Rakibin en sık oynadığı hamle
            predicted_move = max(counts, key=counts.get)
            if predicted_move == "R":
                return "P"
            elif predicted_move == "P":
                return "S"
            elif predicted_move == "S":
                return "R"

    # Hiç veri yoksa random başla (ilk oyun)
    return random.choice(["R","P","S"])


