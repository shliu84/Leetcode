import java.util.Arrays;

/**   
 * 
 * @Title: qsort.java
 * @Prject: temp_912
 * @Package: 
 * @Description: TODO
 * @author: SiHan Liu  
 * @date: 27 Aug 2021 3:51:18 pm
 * @version: V1.0  
 */

/** 
 * @ClassName: qsort
 * @Description: TODO
 * @author: SiHan Liu
 * @date: 27 Aug 2021 3:51:18 pm
 */

public class quicksort {
	/**
	 * 
	 * @Title: sortArray
	 * @Description: TODO
	 * @param nums
	 * @return
	 * @return: int[]
	 */
	public int[] sortArray(int[]nums) {
		if(nums.length<2) {
			return nums;
		}
		else {
			int l = 0;
			int r = nums.length-1;
			
			nums = qsort(nums, l, r);
			
			return nums;
		}
		
	}
	
	/**
	 * 
	 * @Title: qsort
	 * @Description: TODO
	 * @param nums
	 * @param l
	 * @param r
	 * @return
	 * @return: int[]
	 */
	public int[] qsort(int[]nums, int l, int r) {
		if(l<r) {
			int i = partition(nums, l, r);
//			System.out.println(l+" "+r+" "+i+" "+Arrays.toString(nums));
			qsort(nums, l, i-1);
			qsort(nums, i+1, r);
			return nums;
		}
		else {
//			System.out.println(l+" "+r+" "+Arrays.toString(nums));
			return nums;
		}
	}

	/**
	 * 
	 * @Title: partition
	 * @Description: TODO
	 * @param nums
	 * @param l
	 * @param r
	 * @return
	 * @return: int
	 */
	public int partition(int[] nums, int l, int r) {
		if(l<r) {
			int pivot = nums[l];
			int pivotIndex = l;
			l = l + 1;
			
			while(r>l) {
				for(;nums[r]>=pivot && l<r;r--) {
					
				}

				for(;nums[l]<pivot && l<r;l++) {
					
				}
//				System.out.println(l+Arrays.toString(nums));
				swap(l,r,nums);
//				System.out.println(l+Arrays.toString(nums));
			}
			if(nums[l]<pivot) {
				swap(pivotIndex, l, nums);
			}else {
				l = pivotIndex;
			}
			
			return l;
		}
		else {
			return l;
		}
			
	}
	
	/**
	 * 
	 * @Title: swap
	 * @Description: TODO
	 * @param a
	 * @param b
	 * @param nums
	 * @return
	 * @return: int[]
	 */
	public int[] swap(int a, int b, int[]nums) {
		int temp = nums[a];
		nums[a]=nums[b];
		nums[b]=temp;
		return nums;
	}
	
	/**
	 * 
	 * @Title: main
	 * @Description: TODO
	 * @param args
	 * @return: void
	 */
	public static void main(String[] args) {
		quicksort s = new quicksort();
		int[] nums = new int[] {7,2,4,3,4,6,5,3,1};
		System.out.println("unsorted: " + Arrays.toString(nums));

		nums = s.sortArray(nums);
		System.out.println("sorted: " +Arrays.toString(nums));
	}

}
