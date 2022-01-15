from django.shortcuts import render, redirect
from django.views import View
from .models import Shops, ShoppingRecords

query = []


class IndexView(View):

    def get(self, request):
        """访问商场主页"""
        if not request.user.is_authenticated:
            return redirect('/login/login')
        else:
            query = Shops.objects.all()
            # print(query[0].shops_id)
            # print(len(query))
            dict={ "shop_id1": query[0].shops_id, "shop_price1": query[0].price,
       "shop_stock1": query[0].stock, "shop_name1": query[0].name, "shop_id2": query[1].shops_id, "shop_price2": query[1].price,
       "shop_stock2": query[1].stock, "shop_name2": query[1].name, "shop_id3": query[2].shops_id, "shop_price3": query[2].price,
       "shop_stock3": query[2].stock, "shop_name3": query[2].name, "shop_id4": query[3].shops_id, "shop_price4": query[3].price,
       "shop_stock4": query[3].stock, "shop_name4": query[3].name, "shop_id5": query[4].shops_id, "shop_price5": query[4].price,
       "shop_stock5": query[4].stock, "shop_name5": query[4].name}
            return render(request, 'index.html', dict)

    def post(self, request):
        shopid = request.POST.get('shopid')
        nums = request.POST.get('nums')
        uid = int(request.user.id)
        total = 0
        for i in range(0,len(query)):
            if query[i].shops_id == shopid:
                total = nums * query[i].price

        ShoppingRecords.objects.create(shops_id=shopid, id=request.user.id, nums=nums, total=total)
        # try:
        #     ShoppingRecords.objects.create(shops_id=shopid, id=request.user.id, nums=nums, total=total)
        # except Exception as e:
        #     return render(request, 'index.html', {'shopping_error': '购买失败'})

        return redirect('/home/home')

