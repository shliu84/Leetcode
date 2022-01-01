
/**  

 * @Title: DoublePointer.java

 * @Prject: leetcode

 * @Package: implement_strStr_028

 * @Description: TODO

 * @author: SiHan Liu  

 * @date: 3 Aug 2021 4:31:47 pm

 * @version: V1.0  

 */
package implement_strStr_028;


/**

 * @ClassName: DoublePointer

 * @Description: TODO

 * @author: SiHan Liu

 * @date: 3 Aug 2021 4:31:47 pm


 */
public class DoublePointer {
	public int strStr(String haystack, String needle) {
		int hLen = haystack.length();
		int nLen = needle.length();
		// return if needle shorter than hay
		if (nLen == 0) return 0;

		if (hLen < nLen)
			return -1;
		
		// compare the substring
		for (int i = 0; i<(hLen - nLen + 1); i++) {	
			for(int j = 0; j < nLen; j++) {
				if(haystack.charAt(i+j)!=needle.charAt(j))
					//break if char at needle not match haystack
					break;
				if(j == nLen - 1) 
					//return if all match
					return i;
			}
		}
		return -1;

	}

	public static void main(String[] args) {
		DoublePointer s = new DoublePointer();

		int a = s.strStr("Hello", "ll");
		System.out.print(a);
	}

}

/*
 * Result: Runtime: 1434 ms, faster than 17.21% of Java online submissions for
 * Implement strStr(). Memory Usage: 38.9 MB, less than 51.74% of Java online
 * submissions for Implement strStr().
 */

/*
 * Comment: this method is slower, but use less memory than the built-in equal()
 * method
 */
