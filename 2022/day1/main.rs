fn p1() {
        let elves = include_str!("input.txt").split("\n\n");
        

        let ans = elves
                .map(
                        |n| n.lines().map( |i| i.parse::<u32>().unwrap()).sum::<u32>()
                ).max().unwrap();

        println!("{}", ans);
}

pub trait RemoveItem {
        fn remove_item(self, item: u32) -> Self;
}

impl RemoveItem for Vec<u32> {
        fn remove_item(mut self, item: u32) -> Self {
                let index = self.iter().position(|i| *i == item).unwrap();
                self.remove(index);
                self
        }
}

fn p2() {
        let elves: Vec<u32> = include_str!("input.txt")
                .split("\n\n")
                .map(|n| n.lines().map(|i| i.parse::<u32>().unwrap()).sum::<u32>()).collect();

        let first = elves.iter().max().unwrap();
        elves = elves.remove(*first); 

        let second = elves.iter().max().unwrap(); 
        elves = elves.remove(*second); 

        let third = elves.iter().max().unwrap();

        println!("{}", first+second+third)
}


fn main() {
        p1();
        p2();
}