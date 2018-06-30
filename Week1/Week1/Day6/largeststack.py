import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.util.*;

import static org.junit.Assert.*;

public class Solution {

    public static class MaxStack {
        ArrayList <Integer>arrlst;
        int max;
        int count;
        MaxStack()
        {
            arrlst= new ArrayList();
            count=0;
        }

        

        public int pop() {
            int temp=arrlst.remove(count-1);
            if(temp<0)
            {
                int dummy= max;
                max=max+temp;
                temp=dummy;
            }
            else if(temp==0)
            {
                temp=max;   
            }
            else
            {
                temp=max-temp;
            }
            count--;
            return temp;
        }

        public void push(int item) {
            if(count==0)
            {
                max=item;
                arrlst.add(item-max);
            }
            else
            {
                int temp=max-item;
                if(temp <0)
                {
                    max=item;
                }
                arrlst.add(temp);
            }
            count++;
        }

        public int getMax() {
            return max;
        }
    }
    






