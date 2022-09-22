def preorder(arrY, answer):
    node = arrY[0]
    arrY1 = []
    arrY2 = []
    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])
    answer.append(node[2])
    print(answer, arrY)
    if len(arrY1) > 0:
        preorder(arrY1, answer)
    if len(arrY2) > 0:
        preorder(arrY2, answer)
    return


def postorder(arrY, answer):
    node = arrY[0]
    arrY1 = []
    arrY2 = []
    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])

    if len(arrY1) > 0:
        postorder(arrY1, answer)
    if len(arrY2) > 0:
        postorder(arrY2, answer)
    answer.append(node[2])


def solution(nodeinfo):
    preanswer = []
    postanswer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    print(nodeinfo)

    arrY = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    arrX = sorted(nodeinfo)

    print(arrY)
    print(arrX)
    preorder(arrY, preanswer)
    postorder(arrY, postanswer)
    return [preanswer, postanswer]