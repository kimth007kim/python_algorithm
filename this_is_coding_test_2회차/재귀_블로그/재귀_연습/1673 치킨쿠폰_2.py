n,k=map(int,input().split())

sorder=0            #총 주문의 수

def chicken(coupon):
    global sorder
    if coupon==0:   #쿠폰 모두 소진시 종료
        return
    if coupon >=k:  #현재 쿠폰이 쿠폰으로 변환 가능한 도장의 수보다 많을경우
        order = coupon//3 *k
        sorder+=order
        coupon+=coupon//k
        coupon-=order
    else:
        sorder+=coupon
        coupon=0
    chicken(coupon)

chicken(n)

print(sorder)