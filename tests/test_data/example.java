/*
*  BSD 3-Clause License
*
*  Copyright (c) 2017, mjclarke01
*  All rights reserved.
*
*  Redistribution and use in source and binary forms, with or without
*  modification, are permitted provided that the following conditions are met:
*
*  * Redistributions of source code must retain the above copyright notice, this
*  list of conditions and the following disclaimer.
*
*  * Redistributions in binary form must reproduce the above copyright notice,
*  this list of conditions and the following disclaimer in the documentation
*  and/or other materials provided with the distribution.
*
*  * Neither the name of the copyright holder nor the names of its
*  contributors may be used to endorse or promote products derived from
*  this software without specific prior written permission.
*
*  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
*  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
*  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
*  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
*  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
*  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
*  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
*  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
*  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
*  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

package org.example.something;

/**
 * This is the main class
 */
public class Main {

    /**
     * Returns the sum of two integers.
     *
     * @param a first integer
     * @param b second integer
     * @return the sum
     */
    static int addTwoNumbers(int a, int b) {
        return a + b;
    }

    /**
     * Prints the given month as a string.
     *
     * @param month the number of the month
     */
    static void printMonthAsString(int month) {
        String monthStr;

        switch (month) {
            case 1:  monthStr = "January";
                break;
            case 2:  monthStr = "February";
                break;
            case 3:  monthStr = "March";
                break;
            case 4:  monthStr = "April";
                break;
            case 5:  monthStr = "May";
                break;
            case 6:  monthStr = "June";
                break;
            case 7:  monthStr = "July";
                break;
            case 8:  monthStr = "August";
                break;
            case 9:  monthStr = "September";
                break;
            case 10: monthStr = "October";
                break;
            case 11: monthStr = "November";
                break;
            case 12: monthStr = "December";
                break;
            default: monthStr = "WTF!";
                break;
        }
        System.out.println(monthStr);
    }

    /**
     * The application starts here.
     *
     * @param args command line input
     */
    public static void main(String[] args) {
        int ans = addTwoNumbers(2, 2);
        System.out.println(ans);

        // Let's print some months
        printMonthAsString(1);

        printMonthAsString(2);

        printMonthAsString(3);
    }
}
