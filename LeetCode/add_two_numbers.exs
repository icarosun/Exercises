# Definition for singly-linked list.
#
# defmodule ListNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           next: ListNode.t() | nil
#         }
#   defstruct val: 0, next: nil
# end

defmodule Solution do
  @spec add_two_numbers(l1 :: ListNode.t | nil, l2 :: ListNode.t | nil) :: ListNode.t | nil
  def add_two_numbers(l1, l2) do
    add(l1, l2, 0)
  end

  def add(nil, nil, next_unity) do
    if next_unity > 0 do
        %ListNode{
            val: next_unity,
            next: nil
        }
    end
  end

  def add(nil, list2, next_unity) do
    sum = list2.val + next_unity
    next_unity = div(sum, 10)
    sum = rem(sum, 10)

    %ListNode{
        val: sum, 
        next: add(nil, list2.next, next_unity)
    }
  end

  def add(list1, nil, next_unity) do
    sum = list1.val + next_unity
    next_unity = div(sum, 10)
    sum = rem(sum, 10)

    %ListNode{
        val: sum, 
        next: add(list1.next, nil, next_unity)
    }
  end

  def add(list1, list2, next_unity) do
    sum = list1.val + list2.val + next_unity
    next_unity = div(sum, 10)
    sum = rem(sum, 10)

    %ListNode{
        val: sum, 
        next: add(list1.next, list2.next, next_unity)
    }
  end
end
