input_text="2\n\n4\napple 10\nbanana 20\napple 53\npear 40\n\n5\nbanana 20\napple 100\napple 33\nbanana 40\nbanana 50"
import numpy as np
def rt_case(input_text):
    text=input_text.split("\n")
    num_of_case=int(text[0])
    text=text[2:]+["\n"]
    start_case=0
    new_text=""
    for i in range(len(text)):
        if start_case>num_of_case:
            break
        if text[i].isdigit():
            enter_number=int(text[i])
            start=0
            statistic={}
            continue
        if text[i].strip()=="":
            line_text=""
            for item,price_list in statistic.items():
                max_price=max(price_list)
                average_price=np.mean(price_list)
                min_price=min(price_list)
                line_text=line_text+"{0} {1} {2} {3}\n".format(item,max_price,min_price,int(average_price))
            new_text=new_text+"Case #{0}\n{1}\n".format(start_case+1,line_text)
            start_case+=1
            continue

        data=text[i].split(" ")
        if start>enter_number:
            continue
        if data[0] not in statistic.keys():
            statistic[data[0]]=[int(data[1])]
        else:
            statistic[data[0]].append(int(data[1]))
        start+=1
    return new_text





print(rt_case(input_text))
if not root:
            return [True, count]
 
        [left, count] = self.isUnivalSubtrees(root.left, count)
        [right, count] = self.isUnivalSubtrees(root.right, count)
        if self.isSame(root, root.left, left) and \
           self.isSame(root, root.right, right):
                count += 1
                return [True, count]
 
        return [False, count]
 
    def isSame(self, root, child, is_uni):
        return not child or (is_uni and root.val == child.val)