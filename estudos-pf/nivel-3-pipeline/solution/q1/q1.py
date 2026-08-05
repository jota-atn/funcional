def soma_notas_aprovados(seq_turmas: list[list], N: int, MEDIA_MIN: float) -> float:
    turmas_grandes = (t for t in seq_turmas if len(t) >= N)
    medias = (sum(t) / len(t) for t in turmas_grandes)
    aprovadas = (m for m in medias if m >= MEDIA_MIN)
    return sum(aprovadas)

