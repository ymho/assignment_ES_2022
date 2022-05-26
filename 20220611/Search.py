def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    left = 0                        # 探索範囲の左端のindex
    right = len(sorted_array) - 1   # 探索範囲の右端のindex

    # 探索範囲が重なるまで、比較を繰り返す
    while left <= right:
        
        mid = (left + right) //2    # 探索範囲の中央のindex(小数切り捨て)

        # 中央の値が探索対象より大きければ、中央より右側を新しい探索範囲とする
        if sorted_array[mid] > target_number:
            right = mid - 1

        # 中央の値が探索対象より小さければ、中央より左側を新しい探索範囲とする                       
        elif sorted_array[mid] < target_number:
            left = mid + 1
        
        # 中央の値が探索対象と等しい場合、そのindexを返却する
        else:
            return mid         
    
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
