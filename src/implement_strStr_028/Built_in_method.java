
/**  

 * @Title: Built_in_method.java

 * @Prject: leetcode

 * @Package: implement_strStr_028

 * @Description: TODO

 * @author: SiHan Liu  

 * @date: 3 Aug 2021 4:22:42 pm

 * @version: V1.0  

 */
package implement_strStr_028;


/**

 * @ClassName: Built_in_method

 * @Description: test built-in indexof() method

 * @author: SiHan Liu

 * @date: 3 Aug 2021 4:22:42 pm


 */
public class Built_in_method {
	
	/**
	
	 * @Title: strStr
	
	 * @Description: built-in method
	
	 * @param haystack
	 * @param needle
	 * @return
	
	 * @return: int
	
	 */
	public int strStr(String haystack, String needle) {
		
		return haystack.indexOf(needle);
	}

	public static void main(String[] args) {
		Built_in_method s = new Built_in_method();

		int a = s.strStr("Heello", "ll");
		System.out.print(a);
	}

}

/*
 * Result: Runtime: 320 ms, faster than 39.74% of Java online submissions for
 * Implement strStr(). Memory Usage: 39.1 MB, less than 35.39% of Java online
 * submissions for Implement strStr().
 */

