module spec GHC.Classes where

import GHC.Types

not     :: x:GHC.Types.Bool -> {v:GHC.Types.Bool | ((v) <=> ~(x))}
(&&)    :: x:GHC.Types.Bool -> y:GHC.Types.Bool
        -> {v:GHC.Types.Bool | ((v) <=> ((x) && (y)))}
(||)    :: x:GHC.Types.Bool -> y:GHC.Types.Bool
        -> {v:GHC.Types.Bool | ((v) <=> ((x) || (y)))}
(==)    :: (GHC.Classes.Eq  a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x = y)}
(/=)    :: (GHC.Classes.Eq  a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x != y)}
(>)     :: (GHC.Classes.Ord a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x > y)}
(>=)    :: (GHC.Classes.Ord a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x >= y)}
(<)     :: (GHC.Classes.Ord a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x < y)}
(<=)    :: (GHC.Classes.Ord a) => x:a -> y:a
        -> {v:GHC.Types.Bool | ((v) <=> x <= y)}

compare :: (GHC.Classes.Ord a) => x:a -> y:a
        -> {v:GHC.Types.Ordering | (((v = GHC.Types.EQ) <=> (x = y)) &&
                                    ((v = GHC.Types.LT) <=> (x < y)) &&
                                    ((v = GHC.Types.GT) <=> (x > y))) }
        
// Note: Unlike the infix relational operators for comparisons, max and min
// are not available for use in reflected functions or in measures. You have
// two options if you need to do this:
// 1. Inline the definition of max or min at the use site (i.e. write it
//    out as if-relop-then-else)
// 2. Redefine max or min and hide the one from the prelude. Mark the replacement
//    with either reflect or inline.
max :: (GHC.Classes.Ord a) => x:a -> y:a -> {v:a | v = (if x > y then x else y) }
min :: (GHC.Classes.Ord a) => x:a -> y:a -> {v:a | v = (if x < y then x else y) }
