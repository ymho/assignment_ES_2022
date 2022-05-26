def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    left = 0                # 整列範囲の左端のindex
    right = len(array) - 1  # 整列範囲の右端のindex

    # 無限ループ
    while True:

        # pivot以上の値までleftを右にずらす。ただし配列のサイズを超えない。
        # 先頭の要素がpivotのため、どんなarrayにもこの値は存在する(※)
        while array[left] < pivot and left < len(array):      
            left += 1

        # pivot未満の値までrightを左にずらす。ただし0を下回らない。
        while array[right] >= pivot and right >= 0:
            right -= 1
        
        # 左右が衝突していれば交換をせずにループを抜ける。
        # そうでなければ値を入れ替えてループを継続する
        if left > right:
            break
        else:
            array[right], array[left] = array[left], array[right]

    # less: pivot未満のグループ、more: pivot以上のグループ
    less = array[:right+1]
    more = array[left:]

    # arrayにpivot未満の値が存在しない場合、lessの長さは0になる。
    # このとき、moreのpivotのindexより大きい部分のみを再帰的にsortする
    # そうでない場合、lessとmoreそれぞれに対して再帰的にsortする。
    # なお、※によりarrayにpivod以上の値が存在しない場合は起こり得ない。

    if len(less) == 0:
        array = [more[0]] + sort(more[1:])
    else:
        array = sort(less) + sort(more)

    return array
    # ここまで記述

if __name__ == '__main__':
    main()
