/ *
Task:
Basic
Block:
In: ["CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA", "BLOCK:amount > 100", ]
Out: 0
Compound
Block:
In: ["CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA", "ALLOW:amount<100",
     "BLOCK:card_country != ip_country AND amount > 100", ]
Out: 0
* /

public


class RadarRules{
public static void main(String[] args) {
String[] values = "CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA,ALLOW:amount<100,BLOCK:card_country != ip_country AND amount > 100,".split(",");
String[] data = values[0].split("&");
Charge charge = new Charge();
charge.setValues(data[0].substring(data[0].indexOf("=")+1, data[0].length()),
data[1].substring(data[1].indexOf("=")+1, data[1].length()),
Integer.parseInt(data[2].substring(data[2].indexOf("=")+1, data[2].length())),
data[3].substring(data[3].indexOf("=")+1, data[3].length()));
int threshold = Integer.parseInt(values[1].substring(values[1].indexOf("amount")+7, values[1].length()));

if (values[1].toLowerCase().contains("allow")){
if (threshold > charge.getAmount()){
if (values.length >= 2){
if (values[2].contains(charge.getCardCountry() + " != " + charge.getIpCountry() + " AND ")){
if (!charge.getCardCountry().equals(charge.getIpCountry()) & & charge.getAmount() > Integer.parseInt(values[2].replaceAll("[^0-9]", ""))){
if (values[2].toLowerCase().contains("block")){
System.out.println(0);
} else if (values[2].toLowerCase().contains("allow")){
System.out.println(1);
}
}
}
}

}
else if (values[1].toLowerCase().contains("<")){
if (charge.getAmount() > threshold){
System.out.println(1);
}
} else if (values[1].toLowerCase().contains("==")){
if (charge.getAmount() == threshold){
System.out.println(1);
}
} else if (values[1].toLowerCase().contains("!=")){
if (charge.getAmount() != threshold){
System.out.println(1);
}
}
} else if (values[1].toLowerCase().contains("block")){
if (values[1].toLowerCase().contains(">")){
if (charge.getAmount() > threshold){
System.out.println(0);
}
} else if (values[1].toLowerCase().contains("<")){
if (charge.getAmount() < threshold){
System.out.println(0);
}
} else if (values[1].toLowerCase().contains("==")){
if (charge.getAmount() == threshold){
System.out.println(0);
}
} else if (values[1].toLowerCase().contains("!=")){
if (charge.getAmount() != threshold){
System.out.println(0);
}
}
}

}

}


class Charge{
private String card_country;
private String currency;
private int amount;
private String ip_country;

public Charge (){
}

public void setValues(String card_country, String currency, int amount, String ip_country){
this.card_country = card_country;
this.currency = currency;
this.amount = amount;
this.ip_country  = ip_country;
}

public String getCardCountry(){


return this.card_country;
}

public
String
getIpCountry()
{
return this.ip_country;
}

public
int
getAmount()
{
return this.amount;
}
}





'''
Stripe Coding Challenge 16/11/2018

I was asked to code a simple "Radar" that will check if a transaction was allowed or not.

Given a string :

String charge = "["CHARGE:card_country=US&currency=USD&amount=250&ip_country=CA","ALLOW:amount>500", ]"
the algorithm has to return 1 of the transaction is allowed and 0 if not.
We have 2 different family rules : ALLOW and BLOCK, and both of them can accept up to 2 rules separated by an OR or an AND.
We have 6 different operations ( >, <, >=, <=, ==, !=)

Improvements

Using regex to process the initial string
Reduce the boilerplate code
Taking in consideration the edge case where we have rules like : "ALLOW:amount>500ANDamount<2000"
FeedBack

I couldn't finish in 1h15 because I am not familiar with regex, which forced me to use different tricks that are very time consuming. But I had a lot of fun trying to solve this problem even if my solution is not the best.

Thanks

Special thanks to Stripe that gave me the chance to take this challenge.
And HackerRank that provided a nice user experience with their online IDE.
'''



import java.util.HashMap;



public class Main {

    public static void main(String[] args) {
        String charge = "[\"CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA\",\"ALLOW:amount>500ANDip_country==CA\",\"BLOCK:card_country==CAORcard_country==MA\",  ]\n";
        String charge1 = "[\"CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA\",\"ALLOW:amount>500ANDip_country==CA\",\"BLOCK:card_country==USANDamount<200\",  ]\n";
        String charge2 = "[\"CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA\",\"ALLOW:currency==EUR\",  ]\n";
        String charge3 = "[\"CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA\",\"BLOCK:amount>500\",  ]\n";

        System.out.println(isAllowed(charge));
        System.out.println(isAllowed(charge1));
        System.out.println(isAllowed(charge2));
        System.out.println(isAllowed(charge3));

    }

    private static int isAllowed(String charge){

        HashMap<Integer,String> operatorMap = new HashMap<>();
        operatorMap.put(1,"==");
        operatorMap.put(2,"!=");
        operatorMap.put(3,"<");
        operatorMap.put(4,"<=");
        operatorMap.put(5,">=");
        operatorMap.put(6,">");

        // this map gives a key to every operator


        /* We split the initial String at " so that we will have an array that looks like :
        [ "[" ,  "CHARGE:..." ,  "," , "ALLOW:..."  ,  "," , "BLOCK:..." ,  "," ]
        so we will use the index [1] to extract the charge info
        the index [3] to extract the ALLOW / BLOCK rules
        and finally index [5] if it exists to extract ALLOW / BLOCK rules
         */
        String[] chargeArray = charge.split("\"");

        /* This first map will contain the charges info for example :
              (key,value) -> (card_country
                        */
        HashMap<String,String> chargeMap = new HashMap<>();

        /* With allowMap will store the Allow rules with their value,
         while allowOperatorMap will store the rule and the index of the operator so that
         we can retrieve the rule completely
         */

        HashMap<String,String> allowMap = new HashMap<>();
        HashMap<String,Integer> allowOperatorMap = new HashMap<>();

        // Same as before but with the block rules

        HashMap<String,String> blockMap = new HashMap<>();
        HashMap<String,Integer> blockOperatorMap = new HashMap<>();


        // AND = 1 ; OR = 2
        int allowOperator = 0;
        int blockOperator = 0;


        /*
        Here we extract the charges info and put them in the map
         */
        String[] ruleArray = chargeArray[1].split(":");
        ruleArray = ruleArray[1].split("&");
        for (String rule : ruleArray) {
            chargeMap.put(rule.split("=")[0],rule.split("=")[1]);
        }

        String[] helper;
        int firstValue = 1;

        /*
        Here we extract the Rules, by doing some string and array manipulations
        then we populate them in the map
         */

        if (chargeArray[3].contains("ALLOW")){
            String[] allowArray = chargeArray[3].split(":");
            allowArray = removeElement(allowArray,0);
            if (chargeArray[3].contains("AND")){
                allowArray = allowArray[0].split("AND");
                allowOperator = 1;
            } else if (chargeArray[3].contains("OR")) {
                allowArray = allowArray[0].split("OR");
                allowOperator = 2;
            }
            for (String s : allowArray){
                helper = s.split(operatorMap.get(returnOperatorValue(s)));
                allowMap.put(helper[0],helper[1]);
                allowOperatorMap.put(helper[0],returnOperatorValue(s));
            }

            /*
            We loop through the rule map and compare the rules with the charge info
             */
            for (String allowRule : allowMap.keySet()){
                if (allowOperator == 1){
                    /*
                    Since the compare function will just return 1 or 0, if we have an AND we can multiply the values
                    and if we have an OR we can summ them and if it's equal to 2(one successful rule)
                    or 3 (2 successful rules) we replace it by 1
                     */

                    //AND
                    firstValue *= compare(chargeMap.get(allowRule),allowMap.get(allowRule),allowOperatorMap.get(allowRule));
                } else if (allowOperator == 2) {
                    //OR
                    firstValue += compare(chargeMap.get(allowRule),allowMap.get(allowRule),allowOperatorMap.get(allowRule));
                } else {
                    //No operation
                    firstValue = compare(chargeMap.get(allowRule),allowMap.get(allowRule),allowOperatorMap.get(allowRule));
                }
            }
            if (allowOperator == 2) firstValue = firstValue == 3?1:firstValue-1;

            // Same thing but for a BLOCK
        } else if (chargeArray[3].contains("BLOCK")) {
            String[] blockArray = chargeArray[3].split(":");
            blockArray = removeElement(blockArray,0);
            if (chargeArray[3].contains("AND")){
                blockArray = blockArray[0].split("AND");
                blockOperator = 1;
            } else if (chargeArray[3].contains("OR")) {
                blockArray = blockArray[0].split("OR");
                blockOperator = 2;
            }
            for (String s : blockArray){
                helper = s.split(operatorMap.get(returnOperatorValue(s)));
                blockMap.put(helper[0],helper[1]);
                blockOperatorMap.put(helper[0],returnOperatorValue(s));
            }

            for (String blockRule : blockMap.keySet()){

                if (blockOperator == 1){
                    //AND
                    firstValue *= compare(chargeMap.get(blockRule),blockMap.get(blockRule),blockOperatorMap.get(blockRule));
                } else if (blockOperator == 2) {
                    //OR
                    firstValue += compare(chargeMap.get(blockRule),blockMap.get(blockRule),blockOperatorMap.get(blockRule));
                } else {
                    //No operation
                    firstValue = compare(chargeMap.get(blockRule),blockMap.get(blockRule),blockOperatorMap.get(blockRule));
                }
            }
            if (blockOperator == 2) firstValue = firstValue == 3?1:firstValue-1;

            //the only difference is that we have to store the opposite value compared to an Allow
            firstValue = firstValue == 1 ? 0 : 1;
        }

        // Same but here we have an ALLOW and a BLOCK
        if (chargeArray.length>5){
            int secondValue = 1;
            if (chargeArray[5].contains("ALLOW")){
                String[] allowArray = chargeArray[5].split(":");
                allowArray = removeElement(allowArray,0);
                if (chargeArray[5].contains("AND")){
                    allowArray = allowArray[0].split("AND");
                    allowOperator = 1;
                } else if (chargeArray[5].contains("OR")) {
                    allowArray = allowArray[0].split("OR");
                    allowOperator = 2;
                }
                for (String s : allowArray){
                    helper = s.split(operatorMap.get(returnOperatorValue(s)));
                    allowMap.put(helper[0],helper[1]);
                    allowOperatorMap.put(helper[0],returnOperatorValue(s));
                }

                for (String allowRule : allowMap.keySet()){
                    if (allowOperator == 1){
                        //AND
                        secondValue *= compare(chargeMap.get(allowRule),allowMap.get(allowRule),allowOperatorMap.get(allowRule));
                    } else if (allowOperator == 2) {
                        //OR
                        secondValue += compare(chargeMap.get(allowRule),allowMap.get(allowRule),allowOperatorMap.get(allowRule));
                    } else {
                        //No operation
                        secondValue = compare(chargeMap.get(allowRule),allowMap.get(allowRule),allowOperatorMap.get(allowRule));
                    }
                }
                if (allowOperator == 2) secondValue = secondValue == 3?1:secondValue-1;

            } else if (chargeArray[5].contains("BLOCK")) {
                String[] blockArray = chargeArray[5].split(":");
                blockArray = removeElement(blockArray,0);
                if (chargeArray[5].contains("AND")){
                    blockArray = blockArray[0].split("AND");
                    blockOperator = 1;
                } else if (chargeArray[5].contains("OR")) {
                    blockArray = blockArray[0].split("OR");
                    blockOperator = 2;
                }
                for (String s : blockArray){
                    helper = s.split(operatorMap.get(returnOperatorValue(s)));
                    blockMap.put(helper[0],helper[1]);
                    blockOperatorMap.put(helper[0],returnOperatorValue(s));
                }

                for (String blockRule : blockMap.keySet()){
                    if (blockOperator == 1){
                        //AND
                        secondValue *= compare(chargeMap.get(blockRule),blockMap.get(blockRule),blockOperatorMap.get(blockRule));
                    } else if (blockOperator == 2) {
                        //OR
                        secondValue += compare(chargeMap.get(blockRule),blockMap.get(blockRule),blockOperatorMap.get(blockRule));
                    } else {
                        //No operation
                        secondValue = compare(chargeMap.get(blockRule),blockMap.get(blockRule),blockOperatorMap.get(blockRule));
                    }
                }
                if (blockOperator == 2) secondValue = secondValue == 3?1:secondValue-1;
                secondValue = secondValue == 1 ? 0 : 1;
            }
            //if we have an Allow and a Block
            return secondValue*firstValue;
        } else {
            // If we have just an Allow or a Block
            return firstValue;
        }
    }

    // helper function that returns an operator value given the operator as a string
    private static int returnOperatorValue(String s){
        HashMap<Integer,String> operatorMap = new HashMap<>();
        operatorMap.put(1,"==");
        operatorMap.put(2,"!=");
        operatorMap.put(3,"<");
        operatorMap.put(4,"<=");
        operatorMap.put(5,">=");
        operatorMap.put(6,">");
        for (Integer i : operatorMap.keySet()){
            if (s.contains(operatorMap.get(i))){
                return i;
            }
        }
        return 0;
    }

    // helper function that compares two strings using one of the six operators
    private static int compare(String s1, String s2, int operatorValue){
        int result = 1;

        switch (operatorValue){
            case 1: result = s1.compareTo(s2)==0?1:0;
            break;
            case 2: result = s1.compareTo(s2)==0?0:1;
            break;
            case 3: result = Integer.parseInt(s1) < Integer.parseInt(s2)? 1 : 0;
            break;
            case 4: result = Integer.parseInt(s1) <= Integer.parseInt(s2)? 1 : 0;
            break;
            case 5: result = Integer.parseInt(s1) >= Integer.parseInt(s2)? 1 : 0;
            break;
            case 6: result = Integer.parseInt(s1) > Integer.parseInt(s2)? 1 : 0;
            break;
        }

        return result;
    }

    // helper function to remove an element from an array
    private static String[] removeElement(String[] arr, int index){
        String[] result = new String[arr.length-1] ;

        for (int i = 0;i<arr.length;i++){
            if (i<index){
                result[i] = arr[i];
            } else if (i>index){
                result[i-1] = arr[i];
            }
        }

        return result;
    }

    public static void printArray (String[] arr){
        for (String s : arr){
            System.out.println(s);
        }
    }
}