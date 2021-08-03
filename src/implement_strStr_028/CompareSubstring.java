
/**  

 * @Title: CompareSubstring.java

 * @Prject: leetcode

 * @Package: implement_strStr_028

 * @Description: https://leetcode.com/problems/implement-strstr/

 * @author: SiHan Liu  

 * @date: 3 Aug 2021 4:07:11 pm

 * @version: V1.0  

 */
package implement_strStr_028;


/**

 * @ClassName: CompareSubstring

 * @Description: Compare substring one by one

 * @author: SiHan Liu

 * @date: 3 Aug 2021 4:07:11 pm


 */
public class CompareSubstring {
	
	/**
	
	 * @Title: strStr
	
	 * @Description: compare
	
	 * @param haystack
	 * @param needle
	 * @return
	
	 * @return: int
	
	 */
	public int strStr(String haystack, String needle) {
        int hLen = haystack.length();
        int nLen = needle.length();
        // return if needle shorter than hay
        if (nLen == 0) return 0;

        if (hLen < nLen)
            return -1;

        // compare the substring
        for (int i = 0; i < (hLen - nLen) + 1; i++) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                if (haystack.substring(i, i + nLen).equals(needle))
                    return i;
                
            }
            
        }
        return -1;

    }
	
    
    /**
    
     * @Title: main
    
     * @Description: test
    
     * @param args
    
     * @return: void
    
     */
    public static void main(String[] args) {
        CompareSubstring s = new CompareSubstring();

        int a = s.strStr("Hello", "ll");
        System.out.print(a);
    }
	

}
